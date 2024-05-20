import itertools
import numpy as np
import pandas as pd
import torch as torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, roc_auc_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from collections import OrderedDict, namedtuple, defaultdict

PATH='D:\code\Python\Autoint\model\save.pt'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def get_auc(loader, model):
    pred, target = [], []
    model.eval()
    with torch.no_grad():#测试集不进入梯度下降
        for x, y in loader:
            x, y = x.to(device).float(), y.to(device).float()
            y_hat = model(x)
            pred += list(y_hat.cpu().numpy())
            target += list(y.cpu().numpy())
    auc = roc_auc_score(target, pred)
    return auc
class DNN(nn.Module):
    def __init__(self, inputs_dim, hidden_units, dropout_rate, ):
        super(DNN, self).__init__()
        self.inputs_dim = inputs_dim
        self.hidden_units = hidden_units
        self.dropout = nn.Dropout(dropout_rate)
        self.hidden_units = [inputs_dim] + list(self.hidden_units)
        self.linear = nn.ModuleList([
            nn.Linear(self.hidden_units[i], self.hidden_units[i + 1]) for i in range(len(self.hidden_units) - 1)
        ])
        for name, tensor in self.linear.named_parameters():
            if 'weight' in name:
                nn.init.normal_(tensor, mean=0, std=0.0001)

        # self.bn = nn.ModuleList([
        #     nn.Linear(self.hidden_units[i], self.hidden_units[i + 1]) for i in range(len(self.hidden_units) - 1)
        # ])
        self.activation = nn.ReLU()

    def forward(self, X):
        inputs = X
        for i in range(len(self.linear)):
            fc = self.linear[i](inputs)
            fc = self.activation(fc)
            fc = self.dropout(fc)
            inputs = fc
        return inputs


class InteractingLayer(nn.Module):
    def __init__(self, embedding_size, head_num=8, use_res=True, scaling=False):
        super(InteractingLayer, self).__init__()
        self.att_embedding_size = embedding_size // head_num
        self.head_num = head_num#多头的头数
        self.use_res = use_res#残差开启
        self.scaling = scaling
#初始化矩阵，w,k,v
        self.W_Query = nn.Parameter(torch.Tensor(embedding_size, embedding_size))
        self.W_Key = nn.Parameter(torch.Tensor(embedding_size, embedding_size))
        self.W_Value = nn.Parameter(torch.Tensor(embedding_size, embedding_size))

        if self.use_res:
            self.W_Res = nn.Parameter(torch.Tensor(embedding_size, embedding_size))#nn.Parameter可以看作是一个类型转换函数，将一个不可训练的类型 Tensor 转换成可以训练的类型 parameter ，并将这个 parameter 绑定到这个module 里面
        for tensor in self.parameters():
            nn.init.normal_(tensor, mean=0.0, std=0.05)

    def forward(self, inputs):

        # inputs: [1024, 26, 4]
        #keys: [1024, 26, 4]
        querys = torch.tensordot(inputs, self.W_Query, dims=([-1], [0]))
        keys = torch.tensordot(inputs, self.W_Key, dims=([-1], [0]))
        values = torch.tensordot(inputs, self.W_Value, dims=([-1], [0]))
        #计算kqv三个矩阵
        # keys: [2, 1024, 26, 2]

        querys = torch.stack(torch.split(querys, self.att_embedding_size, dim=2))#将querys矩阵按照size,因为是多头注意力，所以切分的大小是embeddingsize//head_num，然后再合回去
        keys = torch.stack(torch.split(keys, self.att_embedding_size, dim=2))
        values = torch.stack(torch.split(values, self.att_embedding_size, dim=2))

        # inner_product: [2, 1024, 26, 26]
        inner_product = torch.einsum('bnik,bnjk->bnij', querys, keys)#求q，k的点积

        if self.scaling:
            #print('!')
            inner_product /= self.att_embedding_size ** 0.5
        self.normalized_att_scores = F.softmax(inner_product, dim=-1)

        # [2, 1024, 26, 2]
        result = torch.matmul(self.normalized_att_scores, values)
        # [1, 1024, 26, 4]
        result = torch.cat(torch.split(result, 1, ), dim=-1)
        # [1024, 26, 4]
        result = torch.squeeze(result, dim=0)
        if self.use_res:
            result += torch.tensordot(inputs, self.W_Res, dims=([-1], [0]))
        result = F.relu(result)
        return result

class AutoInt(nn.Module):
    def __init__(self, feat_size, embedding_size, linear_feature_columns, dnn_feature_columns, att_layer_num=4,
                 att_head_num=8,
                 att_res=True, dnn_hidden_units=(256, 128)):
        super(AutoInt, self).__init__()
        self.sparse_feature_columns = list(filter(lambda x: x[1] == 'sparse', dnn_feature_columns))

        self.embedding_dic = nn.ModuleDict({
            feat[0]: nn.Embedding(feat_size[feat[0]], embedding_size, sparse=False) for feat in
            self.sparse_feature_columns
        })#初始化embedding(稀疏特征)
        self.dense_feature_columns = list(filter(lambda x: x[1] == 'dense', dnn_feature_columns))
        #print(feat_size)
        self.feature_index = defaultdict(int)#默认一个int类型的dict
        start = 0
        for feat in feat_size:#为特征编号
            self.feature_index[feat] = start
            start += 1
        #print(self.feature_index)
        self.dnn = DNN(len(self.dense_feature_columns) + embedding_size * len(self.embedding_dic), dnn_hidden_units,
                       0.5)#初始化dnn层,长度：连续的列+离散的embedding*离散特征的个数，dnn隐藏单元，dropout值
       # print(dnn_hidden_units[-1])
        self.dnn_linear = nn.Linear(dnn_hidden_units[-1] + embedding_size * len(self.embedding_dic), 1, bias=False)#全连接层，设定输入大小，输出大小，由于是二分类，输出是1

        for name, tensor in self.dnn_linear.named_parameters():#权重矩阵的初始化
            if 'weight' in name:
                nn.init.normal_(tensor, mean=0, std=0.00001)

        dnn_hidden_units = [len(feat_size), 1]
        #将特征归一
        for i in range(len(dnn_hidden_units) - 1):
            print(dnn_hidden_units[i], dnn_hidden_units[i + 1])
        self.linear = nn.ModuleList([
            nn.Linear(dnn_hidden_units[i], dnn_hidden_units[i + 1]) for i in range(len(dnn_hidden_units) - 1)
        ])#建立神经网络层
        for name, tensor in self.linear.named_parameters():
            if 'weight' in name:
                nn.init.normal_(tensor, mean=0, std=0.00001)

        self.int_layers = nn.ModuleList([
            InteractingLayer(embedding_size, att_head_num, att_res) for _ in range(att_layer_num)
        ])

        self.out = nn.Sigmoid()
        self.act = nn.ReLU()
        self.dropout = nn.Dropout(0.5)

    def forward(self, X):
        # X [1024, 39]
        logit = X
        #print(self.embedding_dic)
        for i in range(len(self.linear)):
            fc = self.linear[i](logit)
            fc = self.act(fc)
            fc = self.dropout(fc)
            logit = fc
        # logit [1024, 1]
            #print(X[:, self.feature_index[feat[0]]].long().reshape(X.shape[0], 1, -1).shape)
        sparse_embedding = [
            self.embedding_dic[feat[0]](X[:, self.feature_index[feat[0]]].long()).reshape(X.shape[0], 1, -1)
            for feat in self.sparse_feature_columns]
        sparse_input = torch.cat(sparse_embedding, dim=1)
        sparse_input = torch.flatten(sparse_input, start_dim=1)
        dense_values = [X[:, self.feature_index[feat[0]]].reshape(-1, 1) for feat in self.dense_feature_columns]
        dense_input = torch.cat(dense_values, dim=1)

        # att_input [1024, 26, 4]
        att_input = torch.cat(sparse_embedding, dim=1)
        for layer in self.int_layers:
            att_input = layer(att_input)
        # att_out [1024, 104]
        att_output = torch.flatten(att_input, start_dim=1)
        #print('att_output shape', att_output.shape)

        # dnn_input [1024, 117] 26*4+13
        dnn_input = torch.cat((dense_input, sparse_input), dim=1)
        # deep_out [1024, 128]
        deep_out = self.dnn(dnn_input)
        stack_out = torch.cat((att_output, deep_out), dim=-1)
        #print('stack_out shape', stack_out.shape)
        logit += self.dnn_linear(stack_out)
        #print('logit shape', logit.shape)
        y_pred = torch.sigmoid(logit)
        return y_pred

def autoint_train(batch_size = 1024, lr = 1e-4,wd = 0,epoches = 7, seed = 2022,embedding_size = 64):
    # device = 'cuda:0'
    user_data=pd.read_csv('data/user_5000_info.csv').dropna()
    opera_data=pd.read_csv('data/opera_data_3000s.csv').drop(['opera_link','opera_time','opera_picture_link'],axis=1)
    click_data=pd.read_csv('data/user_5000_opera_3000_rating.csv').drop(['timestamp','index'],axis=1).dropna()
    click_data=pd.merge(click_data,user_data,how='left',on='user_id')
    click_data=pd.merge(click_data,opera_data,how='left',on='opera_id')
    click_data['click']=click_data.apply(lambda x:1 if x['rating']>3 else 0,axis=1)
    click_data.drop(['rating'],axis=1)
    #print(click_data)
    sparse_feature = ['opera_id','user_id','opera_type','opera_name','opera_singer','gender','regional_coding','genres']
    dense_feature = ['age','occupation']
    col_names = ['click']+dense_feature + sparse_feature
    click_data=click_data[col_names]
    # print(col_names)
    #data = pd.read_csv('./data/dac_sample.txt', names=col_names, sep='\t')
    # print(data)
    click_data[sparse_feature] = click_data[sparse_feature].fillna('-1', )
    click_data[dense_feature] = click_data[dense_feature].fillna('0', )
    #target = ['label']

    feat_sizes = {}
    feat_sizes_dense = {feat: 1 for feat in dense_feature}
    feat_sizes_sparse = {feat: len(click_data[feat].unique()) for feat in sparse_feature}  # 统计特征个数
    feat_sizes.update(feat_sizes_dense)
    feat_sizes.update(feat_sizes_sparse)
    #print(feat_sizes)
    for feat in sparse_feature:
        lbe = LabelEncoder()
        click_data[feat] = lbe.fit_transform(click_data[feat])
    nms = MinMaxScaler(feature_range=(0, 1))
    click_data[dense_feature] = nms.fit_transform(click_data[dense_feature])  # 归一化连续特征
    #print(click_data)
    fixlen_feature_columns = [(feat, 'sparse') for feat in sparse_feature] + [(feat, 'dense') for feat in dense_feature]
    # 将sparse和dense类别分开
    #print(fixlen_feature_columns)
    dnn_feature_columns = fixlen_feature_columns
    linear_feature_columns = fixlen_feature_columns

    train, test = train_test_split(click_data, test_size=0.2, random_state=seed)  # 切分数据集
    #print(feat_sizes)
    # device = 'cuda:0'
    model = AutoInt(feat_sizes, embedding_size, linear_feature_columns, dnn_feature_columns).to(device)

    train_label = pd.DataFrame(train['click'])
    train = train.drop(columns=['click'])
    #print(train.columns.tolist())
    train_tensor_data = TensorDataset(torch.from_numpy(np.array(train)), torch.from_numpy(np.array(train_label)))
    #print(torch.from_numpy(np.array(train)))
    #print(torch.from_numpy(np.array(train_label)))
    train_loader = DataLoader(train_tensor_data, shuffle=True, batch_size=batch_size)
    #print(train_tensor_data[0][0].shape)
    test_label = pd.DataFrame(test['click'])
    test = test.drop(columns=['click'])
    test_tensor_data = TensorDataset(torch.from_numpy(np.array(test)), torch.from_numpy(np.array(test_label)))
    test_loader = DataLoader(test_tensor_data, batch_size=batch_size)

    loss_func = nn.BCELoss(reduction='mean')  # 使用交叉熵损失函数，返回平均值
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=wd)  # adam优化器，减少震荡

    for epoch in range(epoches):
        total_loss_epoch = 0.0
        total_tmp = 0
        model.train()  # 切换训练模式
        for index, (x, y) in enumerate(train_loader):
            #print(x)
            x, y = x.to(device).float(), y.to(device).float()
            #print(x.shape)
            #print(x)
            y_hat = model(x)
            optimizer.zero_grad()  # 清零优化器
            loss = loss_func(y_hat, y)  # 计算交叉熵
            loss.backward()  # 反向传播
            optimizer.step()  # 模型更新
            total_loss_epoch += loss.item()
            total_tmp += 1
        auc = get_auc(test_loader, model)
        print('epoch/epoches: {}/{}, train loss: {:.3f}, test auc: {:.3f}'.format(epoch, epoches,
                                                                                  total_loss_epoch / total_tmp, auc))
    torch.save(model, PATH)
# def test_model(user_emmdedding,item_list):
#     model=torch.load(PATH)
#     model.eval()
#     #根据物品id，读取物品信息，与用户emmbedding链接
#     #等数据集
#     out_list=[]
#     fin_emmedding_list=[]
#     for i in range(len(item_list)):
#         fin_emmedding_list.append(''.join([user_emmdedding,item_list[i]]))
#         pre_y=model(fin_emmedding_list[i])
#         if pre_y==1:
#             out_list.append(item_list[i])
#     return out_list
    #model = TheModelClass(*args, **kwargs)
    #model.load_state_dict(torch.load(PATH))

if __name__ == '__main__':
   autoint_train(epoches=6)

