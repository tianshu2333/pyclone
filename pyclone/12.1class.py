import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np
iris = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv')
plt.hist(iris['sepal length'],color='red', alpha=0.5)
plt.hist(iris['petal length'],color='green', alpha=0.5)
plt.show()

sepal_mu = np.mean(iris['sepal length'])
sepal_var = np.var(iris['sepal length'])
sepal_std = np.std(iris['sepal length'])

petal_mu = np.mean(iris['petal length'])
petal_var = np.var(iris['petal length'])
petal_std = np.std(iris['petal length'])


a_s = np.min(iris['sepal length'])
b_s = np.max(iris['sepal length'])
x_s = np.arange(a_s,b_s,0.01)
# y_s = norm.pdf(x_s,loc = sepal_mu, scale= sepal_std)
plt.plot(x_s,norm.pdf(x_s,loc = sepal_mu, scale = sepal_std),lw= 3, color='r')
plt.show()

irisSetosa = iris[iris.iloc[:,2]=='Iris-setosa']
irisVersicolor = iris[iris.iloc[:, 2] == 'Iris-versicolor']
irisVirginica = iris[iris.iloc[:,2]=='Iris-virginica']

irisSetosa_mu = np.mean(iris['petal length'])
# plt.plot(x_s,norm.pdf(x_s,loc = sepal_mu, scale = sepal_std),lw= 3, color='r')


# print(NUM)

