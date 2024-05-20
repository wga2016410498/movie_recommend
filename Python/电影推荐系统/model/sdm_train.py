import pandas as pd
from deepctr.feature_column import SparseFeat, VarLenSparseFeat
from model.preprocess import gen_data_set_sdm, gen_model_input_sdm
from sklearn.preprocessing import LabelEncoder
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Model, save_model
from deepmatch.models import SDM
from deepmatch.utils import sampledsoftmaxloss, NegativeSampler
import tensorflow as tf
if __name__ == "__main__":
    data_path = "../data"
    model_out_file = "../data/SDM.h5"
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    user = pd.read_csv(data_path + '/users.dat', sep='::', header=None, names=unames)
    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_csv(data_path + '/ratings.dat', sep='::', header=None, names=rnames)
    mnames = ['movie_id', 'title', 'genres']
    movies = pd.read_csv(data_path + '/movies.dat', sep='::', header=None, names=mnames)
    data = pd.merge(pd.merge(ratings, movies), user)
    sparse_features = ["movie_id", "user_id","gender", "age", "occupation", "zip", "genres"]
    SEQ_LEN_short = 5
    SEQ_LEN_prefer = 50
    embedding_dim = 32
    if tf.__version__ >= '2.0.0':
        tf.compat.v1.disable_eager_execution()
    features = ['user_id', 'movie_id', 'gender', 'age', 'occupation', 'zip', 'genres']
    feature_max_idx = {}
    for feature in features:
        lbe = LabelEncoder()
        data[feature] = lbe.fit_transform(data[feature]) + 1
        feature_max_idx[feature] = data[feature].max() + 1

    user_profile = data[["user_id", "gender", "age", "occupation", "zip", "genres"]].drop_duplicates('user_id')
    item_profile = data[["movie_id"]].drop_duplicates('movie_id')
    user_profile.set_index("user_id", inplace=True)
    train_set, test_set = gen_data_set_sdm(data, seq_short_len=SEQ_LEN_short, seq_prefer_len=SEQ_LEN_prefer)
    train_model_input, train_label = gen_model_input_sdm(train_set, user_profile, SEQ_LEN_short, SEQ_LEN_prefer)
    test_model_input, test_label = gen_model_input_sdm(test_set, user_profile, SEQ_LEN_short, SEQ_LEN_prefer)

    user_feature_columns = [SparseFeat('user_id', feature_max_idx['user_id'], 16),
                            SparseFeat("gender", feature_max_idx['gender'], 16),
                            SparseFeat("age", feature_max_idx['age'], 16),
                            SparseFeat("occupation", feature_max_idx['occupation'], 16),
                            SparseFeat("zip", feature_max_idx['zip'], 16),
                            VarLenSparseFeat(SparseFeat('short_movie_id', feature_max_idx['movie_id'], embedding_dim,
                                                        embedding_name="movie_id"), SEQ_LEN_short, 'mean',
                                             'short_sess_length'),
                            VarLenSparseFeat(SparseFeat('prefer_movie_id', feature_max_idx['movie_id'], embedding_dim,
                                                        embedding_name="movie_id"), SEQ_LEN_prefer, 'mean',
                                             'prefer_sess_length'),
                            VarLenSparseFeat(SparseFeat('short_genres', feature_max_idx['genres'], embedding_dim,
                                                        embedding_name="genres"), SEQ_LEN_short, 'mean',
                                             'short_sess_length'),
                            VarLenSparseFeat(SparseFeat('prefer_genres', feature_max_idx['genres'], embedding_dim,
                                                        embedding_name="genres"), SEQ_LEN_prefer, 'mean',
                                             'prefer_sess_length'),
                            ]

    item_feature_columns = [SparseFeat('movie_id', feature_max_idx['movie_id'], embedding_dim)]
    K.set_learning_phase(True)
    sampler_config = NegativeSampler(sampler='uniform', num_sampled=2, item_name='item')
    model = SDM(user_feature_columns, item_feature_columns, history_feature_list=['movie_id', 'genres'],
                units=embedding_dim,sampler_config=sampler_config)
    model.compile('adam', sampledsoftmaxloss)
    model.summary()
    history = model.fit(train_model_input, train_label,  # train_label,
                        batch_size=512, epochs=1, verbose=1, validation_split=0.0, )
    model.save_weights('SDM_weights.h5')
    K.set_learning_phase(False)

    # 4. Generate user features for testing and full item features for retrieval
    test_user_model_input = test_model_input
    all_item_model_input = {"movie_id": item_profile['movie_id'].values, }

    user_embedding_model = Model(inputs=model.user_input, outputs=model.user_embedding)
    item_embedding_model = Model(inputs=model.item_input, outputs=model.item_embedding)

    # user_embs = user_embedding_model.predict(test_user_model_input, batch_size=2 ** 12)
    # item_embs = item_embedding_model.predict(all_item_model_input, batch_size=2 ** 12)
    #
    # print(user_embs.shape)
    # print(item_embs.shape)
    #
    # test_true_label = {line[0]: [line[2]] for line in test_set}
    tf.compat.v1.disable_eager_execution()
    save_model(model, model_out_file)
    #
    # # 保存用户向量模型
    # save_model(user_embedding_model, '../data/user_embedding_model.h5')
    #
    # # 保存物品向量模型
    # save_model(item_embedding_model, '../data/item_embedding_model.h5')