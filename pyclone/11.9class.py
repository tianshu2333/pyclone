# e = [["A",52,1.7],['B',75,1.6],["C",73,1.8]]
# # give the origin data
# name=input("Whose BMI do you want?")
# assert  name == "A" or name == "B" or name == "C","Sorry we cannot find this guy LOL"
# if  name==e[0][0]:
#     print(e[0][1]/(e[0][2]*e[0][2]))
#     print('you are soo thin please eat more.')
# elif name==e[1][0]:
#     print(e[1][1] / (e[1][2] * e[1][2]))
#     print('Your BMI is ok, keep it!')
# elif name==e[2][0]:
#     print(e[2][1] / (e[2][2] * e[2][2]))
#     print('You are so heavy, please eat less and do more exercises.')
# else:
#     print("Sorry we cannot find this guy LOL")

# # another topic
# import pandas as pd
# data = pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight_small.csv")
# # print the height
# # print(data.Ht)
# # print(data.Wt)
# # print(data.sex)
# print(data.iloc[1])
# print("John\'s height is {}".format(data.Ht[1]))
#

# pandas
# import pandas as pd
# data_dir = 'C:/Users/lhy12/Desktop/sample/Data/'
# data = pd.read_csv(data_dir+"test.csv")
    # For locate the data
    # form: data.iloc[;]
# print(data.iloc[0])
# print(data.iloc[0:2])
# # 好きな列を見る
# print(data.iloc[:,0])
# print(data.iloc[:,0:3])
#  #指定看坐标
# print(data.columns)
#
# # 項目を指定して見る
# print(data.name)
# print(data.height)
#
# # 項目を指定して好きな行を見る
# print(data.iloc[0].weight)
# print(data.weight[0:2])


# for i in range(data.shape[0]):
#     print(data.iloc[i])
#
# # 行を追加
# s = pd.Series(['Jiro',30,75,180],index=data.columns)
# data = data.append(s,ignore_index=True)
#
# # 新規列名を指定して追加
# data['BMI'] = [20, 30, 25]
# print(data)
#
# # 行、列を指定して編集
# data.iloc[0,4] = 40
# print(data)


# import random
# for i in range(10):
#     number = random.randint(0,10)
#     print(number)
#     if number == 1:
#         print(number)
#         print(("equal"))
#         break
#     else:
#         print(number)
#     
# function related

# def double(num):
#     num = num * 2
#     return  num
# print(double(10))

# def fib(para):
#     if para == 1:
#         x = [0,]
#     elif para == 2:
#         x = [0, 1]
#     else:
#         x = [0, 1]
#         for i in range(para-2):
#             new = x[-2] + x[-1]
#             x.append(new)
#     return x
#
# def plus(num):
#     x = 0
#     for i in range(0,num):
#         x = x + i
#     return x
# print(plus(10))
#
# print(fib(10))

import pandas as pd
import numpy as np
data_dir = 'C:/Users/lhy12/Desktop/sample/Data/'
data = pd.read_csv(data_dir+"height_weight_small2.csv")
# calculate the BMI ex3
BMIs = []
# for i in range(0,10):
#     BMI = data.Wt[i]/(data.Ht[i]*data.Ht[i]/10000)
#     BMI = np.round(BMI)
#     BMIs.append(BMI)
#     print("The BMI of", i , "is {}".format(BMI))
# data['BMI'] = BMIs
# print (data)

def calbmi(i):
    BMI = data.Wt[i] / (data.Ht[i] * data.Ht[i] / 10000)
    BMI = np.round(BMI)
    print(BMI)
    BMIs.append(BMI)
    return BMI
# a = int(input('please input the start:'))
# b = int(input('please input the end:'))
data['BMI'] = 0
for i in range(0,10):
    print(calbmi(i))
    data.BMI[i] = calbmi(i)
    BMIs.append(calbmi(i))



print(BMIs)
print(data)

