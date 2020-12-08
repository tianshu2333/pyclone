import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# class cal:
#     iris=pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv')
#     plt.scatter(iris.iloc[:,0], iris.iloc[:,2])
#     # plt.show()
#     def r(self):
#         iris = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv')
#         self.r = scipy.stats.pearsonr(iris.iloc[:,0],iris.iloc[:,2])
#         return self.r
#     def R(self):
#         iris = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv')
#         self.R = np.corrcoef([iris.iloc[:, 0], iris.iloc[:, 1],
#                          iris.iloc[:, 2], iris.iloc[:, 3]])
#         return self.R
#     # print(r)
#     # print(p)
#     #
#     # return (r,p,R)
# IRIS = cal()
# print(IRIS.r())

from statsmodels import api as sm
import matplotlib.pyplot as plt
import pandas as pd

ais = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/ais.csv')
X = ais.Ht
X = sm.add_constant(X)
Y = ais.Wt
model=sm.OLS(Y,X)
result = model.fit()
result.summary()

plt.scatter(x=ais.Ht,y=ais.Wt) and plt.plot(ais.Ht,model.fit().predict(X),c="red")
plt.show()

unknown = [185, 167, 215, 177]
X2 = sm.add_constant(pd.DataFrame(unknown))
Wt2 = model.fit().predict(X2)
plt.scatter(x=ais.Ht,y=ais.Wt) and plt.plot(ais.Ht,model.fit().predict(X),c="red") and plt.scatter(x=unknown,y=Wt2, c='orange')
plt.show()