import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
iris = pd.read_csv('C:/Users/lhy12/Desktop/sample/Data/iris.csv')
X = iris.drop('class', axis=1)
Y = iris['class']

X_scaled = (X-X.mean())/X.std()

pca = PCA(n_components=2)
pca.fit(X_scaled)
reduced_iris = pca.fit_transform(X_scaled)
colors = ['blue', 'red', 'Yellow']
uniqueY = pd.unique(Y)
for i in range(len(uniqueY)):
    Yi = uniqueY[i]
    color = colors[i]
    plt.scatter(reduced_iris[np.where(Y == Yi), 0],reduced_iris[np.where(Y == Yi), 1],c=color)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()

print(pca.explained_variance_ratio_)

print(pca.components_)