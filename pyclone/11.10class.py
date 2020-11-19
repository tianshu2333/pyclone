import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight.csv")
# print(temper_data.mean())
# print(temper_data.describe())
# temper_data.plot()
# plt.show()
# temper_data.plot(y="Naha",kind='hist')
# plt.show()
#
# a = [1,2,4,5,6,72,3,52,43,23,5,3,3]
# plt.plot(a)
# plt.show()
#
# temper_data.plot(y="Naha",kind='hist')
# temper_data.plot(y="Sapporo",kind='hist')
# temper_data.plot(y="Fukuoka",kind='hist')
# temper_data.plot.hist(bins=10,alpha=0.3)
# temper_data.plot.hist(bins=50,alpha=0.3)
# temper_data.plot.hist(bins=100,alpha=0.3)
#
# plt.show()
# x = np.array([3,5])
# y = np.array([6,1])
# print(x+y)
# print(x-y)
#
# a = np.array([3,5,2])
# b = np.array([6,1,2])
# print(a+b)
# print(a-b)

# 
# x = np.array([60,180])
# y = np.array([60,150])
#
# D = np.dot(x,y); # 内積
# xd = np.linalg.norm(x); #||x||
# yd = np.linalg.norm(y); #||y||
# C = D/(xd*yd); # コサイン類似度
# print(C) # 表示
# 
# a = np.array([3,5])
# b = np.array([6,1])
# c = np.dot(a,b)
# d = c/(np.linalg.norm(x)*np.linalg.norm(y))
# print(d)
# 
# A = np.array([3,5,2])
# B = np.array([6,1,2])
# C = np.dot(A,B)
# D = C/(np.linalg.norm(A)*np.linalg.norm(B))
# print(D)


# f = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/data.csv")
# vlist = np.array(f)
# #决定K
# k = 4
# #step1决定初期的类点
# #决定random的值范围
# a = np.min(vlist[:,0])
# b = np.max(vlist[:,0])
# c = np.min(vlist[:,1])
# d = np.max(vlist[:,1])
# Clist = np.c_[(b-a)*np.random.rand(k) + a, (d-c)*np.random.rand(k)+c]
# plt.scatter(vlist[:0],vlist[:,1])
# plt.scatter(Clist[:,0],Clist[:,1],c='blue',marker='+',s=100)
# orgClist = Clist
# #Kmeans
# def nearest(X,CList):
#     minD = float("inf")
#     minId = 0
#     for ii in range(0,len(CList))
#         C = CList[ii]
#         d = np.linalg.norm(X-C)
#         if d< minD：
#             minD = d
#             minId = ii
#     return minId

a = np.array([180,75])


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

colre = []
for i in range(1,202):
    height = data.iloc[i].Ht
    weight = data.iloc[i].Wt
    b = np.array([height,weight])
    c = np.dot(a, b)
    d = c / (np.linalg.norm(a) * np.linalg.norm(b))
    colre.append(d)
    # print(i,d)
print(colre)
print(bubbleSort(colre))
a = int(input("sadasda"))
b = input("asdas")
c = 1
print(a+c)
print()
str(input())
