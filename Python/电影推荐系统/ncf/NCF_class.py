import pandas as pd
from deepmatch.models import NCF
from tensorflow.keras import Model
from tensorflow.python.keras import backend as K
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from deepctr.layers import custom_objects
import heapq
import random
import json
from tqdm import tqdm
from sklearn.metrics import log_loss, roc_auc_score


class NCF_class:
    def __init__(self):
        self.Recall_topK = 9
        self.negsample = 5

        self.dict_out_file = 'D:\\code\\Python\\电影推荐系统\\movieData\\Dict\\NCF_user_item_topk_dict.npy'
        self.PATH = 'D:\\code\\Python\\电影推荐系统\\movieData\\Model\\NCF.h5'

    def save_model(self,model,PATH):
        model.save(PATH, overwrite=True)
    def read_model(self,PATH):

        model = load_model(PATH, custom_objects)
        return model

    def save_dict_to_json(data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
    def get_user_item_dict(self,user_len, movie_len, user_profile, item_profile):
        model = self.read_model(self.PATH)
        user_item_dict = {}
        for user_id in range(1, user_len):
            users = np.full(movie_len, user_id)
            items = np.arange(1, movie_len + 1, 1)
            labels = np.full(movie_len, 0)
            users = users.reshape(users.shape[0], 1)
            items = items.reshape(items.shape[0], 1)
            labels = labels.reshape(labels.shape[0], 1)
            ans = np.concatenate((users, items, labels), axis=1)
            ans = [tuple(x) for x in ans.tolist()]
            test_model_input, test_label = self.gen_model_input(ans, user_profile, item_profile)
            pred_ans = model.predict(test_model_input, batch_size=256)
            pred_ans = np.array(pred_ans).flatten()
            items = np.array(items).flatten()
            map_item_score = {}  # 存储该user对所有item的分数
            for i in range(len(items)):
                item = items[i]
                map_item_score[item] = pred_ans[i]  # 填充预测分数
            ranklist = heapq.nlargest(self.Recall_topK, map_item_score, key=map_item_score.get)
            user_item_dict[user_id] = ranklist
        return user_item_dict
    def get_user_item_topk_dict(self):
        np.load.__defaults__ = (None, True, True, 'ASCII')
        load_dict = np.load(self.dict_out_file)

        np.load.__defaults__ = (None, False, True, 'ASCII')
        return load_dict
    def gen_data_set(self,data,negsample=0):
        data.sort_values("time_stamp", inplace=True)
        item_ids = data['movie_id'].unique()
        # item_id_genres_map = dict(zip(data['movie_id'].values, data['genres'].values))
        train_set = []
        test_set = []
        for reviewerID, hist in tqdm(data.groupby('user_id')):
            pos_list = hist['movie_id'].tolist()
            if negsample > 0:
                candidate_set = list(set(item_ids) - set(pos_list))
                neg_list = np.random.choice(candidate_set, size=len(pos_list) * negsample, replace=True)
            for i in range(1, len(pos_list)):
                if i != len(pos_list) - 1:
                    train_set.append((
                        reviewerID, pos_list[i], 1
                    ))
                    for negi in range(negsample):
                        train_set.append((reviewerID, neg_list[i * negsample + negi], 0))
                else:
                    test_set.append((reviewerID, pos_list[i], 1))
                    for negi in range(negsample):
                        test_set.append((reviewerID, neg_list[i * negsample + negi], 0))
        random.shuffle(train_set)
        random.shuffle(test_set)
        return train_set, test_set
    def gen_model_input(self,train_set, user_profile, item_profile):
        train_uid = np.array([line[0] for line in train_set])
        train_iid = np.array([line[1] for line in train_set])
        train_label = np.array([line[2] for line in train_set])
        train_model_input = {"user_id": train_uid, "movie_id": train_iid}
        for key in ["gender", "age", "occupation", "regional_coding"]:
            train_model_input[key] = user_profile.loc[train_model_input['user_id']][key].values
        for key in ["tag"]:
            train_model_input[key] = item_profile.loc[train_model_input['movie_id']][key].values
        return train_model_input, train_label
    def Data_load(self):
        data_path = "../movieData/"
        user = pd.read_csv(data_path + 'users.csv')
        ratings = pd.read_csv(data_path + 'ratings.csv')
        movie = pd.read_csv(data_path + 'moviesinfo.csv')
        data = pd.merge(pd.merge(ratings, movie), user)
        # data['genres'] = list(map(lambda x: x.split('|')[0], data['genres'].values))
        features = ['user_id', 'movie_id', 'gender', 'age', 'occupation', 'regional_coding', 'tag']
        feature_max_idx = {}
        for feature in features:
            lbe = LabelEncoder()

            if feature == 'age':
                dict_age = dict(zip(data[feature],lbe.fit_transform(data[feature]) + 1))
            elif feature == 'occupation':
                dict_occupation = dict(zip(data[feature],lbe.fit_transform(data[feature]) + 1))
            elif feature == 'regional_coding':
                dict_regional_coding = dict(zip(data[feature], lbe.fit_transform(data[feature]) + 1))
            data[feature] = lbe.fit_transform(data[feature]) + 1
            feature_max_idx[feature] = data[feature].max() + 1
        user_profile = data[["user_id", "gender", "age", "occupation", "regional_coding"]].drop_duplicates('user_id')
        item_profile = data[["movie_id", "tag"]].drop_duplicates('movie_id')
        user_profile.set_index("user_id", inplace=True)
        item_profile.set_index("movie_id", inplace=True)
        train_set, test_set = self.gen_data_set(data, self.negsample)
        train_model_input, train_label = self.gen_model_input(train_set, user_profile, item_profile)
        test_model_input, test_label = self.gen_model_input(test_set, user_profile, item_profile)
        user_feature_columns = {"user_id": feature_max_idx['user_id'], 'gender': feature_max_idx['gender'],
                                "age": feature_max_idx['age'],
                                "occupation": feature_max_idx["occupation"],
                                "regional_coding": feature_max_idx["regional_coding"]}
        item_feature_columns = {"movie_id": feature_max_idx['movie_id']}
        return dict_age, dict_occupation, dict_regional_coding, user_feature_columns, item_feature_columns, train_model_input, train_label, test_model_input, test_label, data, user_profile, item_profile
    def train(self):
        if tf.__version__ >= '2.0.0':
            tf.compat.v1.disable_eager_execution()
        else:
            K.set_learning_phase(True)

        dict_age, dict_occupation, dict_regional_coding, user_feature_columns, item_feature_columns, train_model_input, train_label, test_model_input, test_label, data, user_profile, item_profile = self.Data_load()
        model = NCF(user_feature_columns, item_feature_columns, user_gmf_embedding_dim=8,
                    item_gmf_embedding_dim=8, user_mlp_embedding_dim=32, item_mlp_embedding_dim=32,
                    dnn_hidden_units=[128, 64, 32])
        model.compile("adam", "binary_crossentropy",
                      metrics=['binary_crossentropy'], )
        model.fit(train_model_input, train_label,
                            batch_size=256, epochs=20, verbose=1)
        self.save_model(model,self.PATH)
        NCF_user_item_dict = self.get_user_item_dict(len(set(data['user_id'])), len(set(data['movie_id'])), user_profile,
                                                item_profile)

        # 将 int32 类型的数组转换为列表
        # for key, value in NCF_user_item_dict.items():
        #     NCF_user_item_dict[key] = value.tolist() if isinstance(value, np.ndarray) else value
        # with open(self.json_file_path, 'w') as json_file:
        #     json.dump(NCF_user_item_dict, json_file)
        np.save(self.dict_out_file, NCF_user_item_dict)

        # user_embedding_model = Model(inputs=model.user_input, outputs=model.user_embedding)
        # self.save_model(user_embedding_model,self.PATH_1)

    def Test_model(self):
        dict_age, dict_occupation, dict_regional_coding,user_feature_columns, item_feature_columns, train_model_input, train_label,test_model_input, test_label,data, user_profile, item_profile = self.Data_load()
        model = self.read_model(self.PATH)
        pred_ans = model.predict(test_model_input, batch_size=64)
        train_auc_g = roc_auc_score(test_label, pred_ans)
        print(train_auc_g)


if __name__ == '__main__':
    ncf = NCF_class()
    # ncf.train()
    # # ncf.Test_model()
    # ncf_user_topk_item = ncf.get_user_item_topk_dict()
    # json_file_path = 'D:\\code\\Python\\电影推荐系统\\movieData\\Dict\\data.json'
    # def convert_to_builtin_type(obj):
    #     if isinstance(obj, np.int32):
    #         return int(obj)
    #     elif isinstance(obj, np.ndarray):
    #         return obj.tolist()
    #     elif isinstance(obj, (list, tuple)):
    #         return [convert_to_builtin_type(item) for item in obj]
    #     elif isinstance(obj, dict):
    #         return {key: convert_to_builtin_type(value) for key, value in obj.items()}
    #     else:
    #         return obj
    # arr_list = ncf_user_topk_item.tolist()
    # with open(json_file_path, 'w') as json_file:
    #     json.dump(convert_to_builtin_type(arr_list), json_file)
    ncf.Test_model()
    # NCF_user_item_dict = ncf.get_user_item_topk_dict()
    # print(NCF_user_item_dict)
    # with open(json_file_path, 'w') as json_file:
    #     json.dump(arr_list, json_file)

    # print(ncf_user_topk_item)
    # print(type(ncf_user_topk_item))
    # with open('D:\\code\\Python\\电影推荐系统\\movieData\\Dict\\data.json', 'w') as f:
    #     json.dump(arr_list, f)
    # ncf.save_dict_to_json(ncf_user_topk_item, 'D:\\code\\Python\\电影推荐系统\\movieData\\Dict\\data.json')
    # ncf_user_list = ncf_user_topk_item.item()[2]
    # print(ncf_user_list)






