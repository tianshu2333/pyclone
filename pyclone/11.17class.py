import matplotlib.pyplot as plt
import matplotlib.cm as cm
# import numpy as np
# data 読み込み
# import pandas as pd
# f = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv', header=None)
# vlist = np.array(f)
# # kの決定
# K = 4;
#
# ## step 1
# def nearest(X,CList):
#     minD = float("inf");
#     minId = 0
#     for ii in range(0,len(CList)):
#         C = CList[ii]
#         d = np.linalg.norm(X-C)
#         if d < minD:
#             minD = d
#             minId = ii
#     return minId
#
# def selectCluster(vlist,CList):
#     cIList = []
#     for row in vlist:
#         cIList.append(nearest(row,CList))
#     return cIList
#
# def updataCenter(vlist,CIList,K):
#     CList = []
#     for k in range(K):
#         Z = []
#         for j in range(len(CIList)):
#             if CIList[j] == k:
#                 Z.append(vlist[j])
#         mc = np.mean(Z,0)
#         CList.append(mc)
#     return CList
#
# # clustering
# # 初期化
# # random値の範囲決定
# a = np.min(vlist[:,0])
# b = np.max(vlist[:,0])
# c = np.min(vlist[:,1])
# d = np.max(vlist[:,1])
# print (a)
# #初期点（K個）をランダムに決定
# CList = np.c_[(b-a)*np.random.rand(K) + a, (d-c)*np.random.rand(K) + c]
# plt.scatter(vlist[:,0], vlist[:,1])
# plt.scatter(CList[:,0], CList[:,1],c='blue',marker='+',s=100)
# orgCList = CList
#
#
# Err = 0.1
# maxittr = 100
# itt = 0
# while itt < maxittr:
#     end_flag = True
#     preCList = CList
#     # 指示クラスタの決定
#     CIList = selectCluster(vlist,CList)
#     # クラスタ中心の更新
#     CList = updataCenter(vlist,CIList,K)
#     # 更新の際の移動距離の算出
#     for j in range(len(CList)):
#         cc = CList[j]
#         pre = preCList[j]
#         dd = np.linalg.norm(cc-pre)
#         print(dd)
#         if dd > Err:
#             end_flag = False
#     itt += 1
#     # 可視化
#     plt.scatter(vlist[:,0], vlist[:,1], c='blue')
#     for k in range(len(CList)):
#         mc = CList[k]
#         plt.scatter(mc[0], mc[1],c='red',marker='+',s=100)
#     plt.show()
#     plt.pause(1)
#     if end_flag == True:
#         break

# from sklearn.cluster import KMeans
# km_model = KMeans(n_clusters=4) #K=4のkmeansモデルの初期化
# km_model.fit(vlist) #実際にデータをクラスタリング
#
# km_model.cluster_centers_ # クラスタの中心たち
#
# labels=km_model.labels_ # 各データがどのクラスタかが入っている
#
# plt.scatter(vlist[:,0], vlist[:,1], c=labels,cmap=cm.Accent)
# plt.show()
########################
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm
# import numpy as np
# import pandas as pd
# from sklearn.cluster import KMeans
# f = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv', header=None)
# vlist = np.array(f)
# km_model = KMeans(n_clusters=3)
# km_model.fit(vlist[1:,0:1])
# km_model.cluster_centers_
# labels = km_model.labels_
# print(labels)
# # between sepal
# # plt.scatter(vlist[1:,0], vlist[1:,1], c=labels,cmap=cm.Accent)
# # between petal
# plt.scatter(vlist[1:,2], vlist[1:,3], c=labels,cmap=cm.Accent)
# #width
# # plt.scatter(vlist[1:,1], vlist[1:,3], c=labels,cmap=cm.Accent)
#
# plt.show()
# ????????
# print(vlaiist[2,1])
# plt.scatter(vlist)


########################
# data = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight.csv")
# a = np.array([180,75])
#
#
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# colre = []
# for i in range(1,202):
#     height = data.iloc[i].Ht
#     weight = data.iloc[i].Wt
#     b = np.array([height,weight])
#     c = np.dot(a, b)
#     d = c / (np.linalg.norm(a) * np.linalg.norm(b))
#     colre.append(d)
#     # print(i,d)
# print(colre)
# print(bubbleSort(colre))
# count = 0
# # 距離の近い順にプロット
# for i in colre:
# row = colre[i]
# # 並び順に応じて色を決定
# c = cm.hot(count/len(vlist))
# # 決定した色を指定してプロット
# plt.scatter(row[2],row[3],color=c)
# count += 1
# # 点Aの可視化
# plt.scatter(A[0], A[1], c=‘green’,
# marker=‘+’, s=60)
#
# import pandas as pd
# import matplotlib.pyplot as plt
# # import numpy as np
# Hw_data = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight.csv")
# plt.hist(Hw_data['Ht'])
# plt.hist(Hw_data['Ht'],bins=30)
# plt.hist(Hw_data['Ht'],bins=50)
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import random
# from scipy.stats import norm
# Wt_data = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight.csv")
# Wt_mu = np.mean(Wt_data['Wt'])
# Wt_var = np.var(Wt_data['Wt'])
# Wt_std = np.std(Wt_data['Wt'])
# a = np.min(Wt_data['Wt']-5)
# b = np.max(Wt_data['Wt']+5)
# x = np.arange(a,b,0.01)
# y = norm.pdf(x,loc = Wt_mu,scale = Wt_std)
# Wt_data.plot(kind="hist",y="Wt",density=True)
# plt.plot(x,y,lw=3,color="r")
# plt.show()

import random
import numpy as np
import matplotlib.pyplot as plt
#
# N = 10000  # 1回の標本中のサンプリング数
# K = 100  # 標本回数
# mu = 0  # 平均
# sigma = 1  # 標準偏差（分散の平方根）
# meanList = []  # 標本平均を保存するリストを初期化
# for j in range(K):  # 標本取得をK回繰り返す
#     samples = []  # サンプルのリスト
#     for i in range(N):  # N個の標本をサンプリング
#         a = random.gauss(mu, sigma)  # 正規分布に従ったランダムサンプリング
#         samples.append(a)
#     sample_mean = np.mean(samples)  # 標本平均の計算
#     meanList.append(sample_mean)  # 標本平均をリストに保存
#
# # ヒストグラムで標本平均の分布を正規化して表示
# plt.hist(meanList, range=[-0.5, 0.5], bins=50, density=True)
# plt.show()
# mu = np.mean(meanList)
# std = np.std(meanList)
# print(mu)
# print(std)
#
#
# import numpy as np
# import pandas as pd
# from scipy import stats
# # data読み込み
# Grade_data=pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/grade_data1.csv",sep=",")
# # 平均と標準偏差を求める
# mu = np.mean(Grade_data['English'])
# sigma = np.std(Grade_data['English'])
# print(mu)
# print(sigma)
# # 母平均の95%信頼区間の推定
# alpha = 0.95 # 信頼係数95%
# n = len(Grade_data['Mathematics']) # sample数
# t = stats.t.ppf(1-(1-alpha)/2, n-1) # t分布を用いて確率変数tを計算
# t_min = mu - t * sigma / np.sqrt(n-1) # 下限
# t_max = mu + t * sigma / np.sqrt(n-1) # 上限
# print(u"信頼区間の下限:",t_min)
# print(u"信頼区間の上限:",t_max)