import pandas as pd
import numpy as np
from data_processing.data_load import load_data

def get_pair_dic():
    drug_s1, target_s1, drug_s2, target_s2, A, pair_index = load_data('../data/nr.xlsx')  # 数据加载
    S_drug = 0.5 * drug_s1 + 0.5 * drug_s2
    S_target = 0.5 * target_s1 + 0.5 * target_s2
    num_drugs, num_targets = A.shape
    print(A.shape)
    features = []
    for i in range(num_drugs):
        for j in range(num_targets):
            # 确保药物和靶标的相似性特征可以连接
            feature = np.concatenate([S_drug[i], S_target[j]])  # 合并药物和靶标的相似性特征
            features.append(feature)
    pair_dic = {}
    for key, value in zip(pair_index, features):
        pair_dic[key] = value
    print(pair_dic)
    pd.DataFrame.from_dict(pair_dic, orient='index').to_csv("../run/pair_dic_nr.csv", index=True, float_format='%.6f')

def get_train_data():
    path1 = '../run/pair_dic_nr.csv'
    path2 = '../run/LapRLS pre.xlsx'
    # 读取 Excel 文件
    pair_data = pd.read_csv(path1)
    pair_data.set_index(pair_data.columns[0], inplace=True)
    data_pre = pd.read_excel(path2, sheet_name='nr')
    # 计算前 5% 和后 5% 的索引位置
    n = len(data_pre)
    top_10_percent_index = int(n * 0.05)
    bottom_10_percent_index = int(n * 0.95)
    positive_index = list(data_pre[:top_10_percent_index]['index'])
    negative_index = list(data_pre[bottom_10_percent_index:]['index'])
    positive_value = pair_data.loc[positive_index].values.tolist()
    negative_value = pair_data.loc[negative_index].values.tolist()

    train_index = positive_index + negative_index
    train_value = positive_value + negative_value

    train_df = pd.DataFrame(train_value, index=train_index)
    labels = [1] * len(positive_index) + [0] * len(negative_index)

    train_df.insert(0, 'label', labels)   # 将第一列替换为label
    print(train_df)
    train_df.to_csv('../run/train_nr.csv', index=True)


def get_test_data():
    path1 = '../data/nr.xlsx'
    path2 = '../run/pair_dic_nr.csv'
    xls = pd.ExcelFile(path1)
    test_index = list(xls.parse("ML_test_index")['ML_test'])
    pair_data = pd.read_csv(path2)
    pair_data.set_index(pair_data.columns[0], inplace=True)

    test_value = pair_data.loc[test_index].values.tolist()
    test_df = pd.DataFrame(test_value, index=test_index)
    test_df.to_csv('../run/test_nr.csv', index=True, float_format='%.6f')

def get_testAll_data():
    path1 = '../data/nr.xlsx'
    path2 = '../run/pair_dic_nr.csv'
    xls = pd.ExcelFile(path1)
    test_index = list(xls.parse("ML_testAll_index")['ML_testAll'])
    pair_data = pd.read_csv(path2)
    pair_data.set_index(pair_data.columns[0], inplace=True)

    test_value = pair_data.loc[test_index].values.tolist()
    test_df = pd.DataFrame(test_value, index=test_index)
    test_df.to_csv('../run/testAll_nr.csv', index=True, float_format='%.6f')




# get_pair_dic()
# get_train_data()
# get_test_data()
# get_testAll_data()



