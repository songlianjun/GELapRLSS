import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2
import pandas as pd
np.set_printoptions(threshold=np.inf)

file_path = '../run/train_enzyme.csv'
df = pd.read_csv(file_path)
print(df)
data_value = df.iloc[:, 2:]
data_value = np.array(data_value)
print(data_value)
print(len(data_value))


X = data_value
y = [1] * int(len(data_value)/2) + [0] * int(len(data_value)/2)

"""梯度提升树特征重要性"""
gb = GradientBoostingClassifier(n_estimators=100, max_features=1000)
gb.fit(X, y)
importances = gb.feature_importances_
print(importances)


"""方差分析 ANOVA"""
fval = f_classif(X, y)
fval = pd.Series(fval[0], index=range(X.shape[1]))
print(fval)

"""卡方检验"""
chi_scores = chi2(X, y)
chi_scores = pd.Series(chi_scores[0], index=range(X.shape[1]))
print(chi_scores)


