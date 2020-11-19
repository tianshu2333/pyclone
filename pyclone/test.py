import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
weight_data=pd.read_csv("C:/Users/lhy12/Desktop/sample/Data/height_weight.csv")
weight_mu = np.mean(weight_data["weight"]) #平均
weight_var = np.var(weight_data["weight"]) #分散：標準偏差の二乗
weight_std = np.std(weight_data["weight"]) #標準偏差

from scipy.stats import norm
weight_data.plot(kind="hist",y="weight",density=True)
import numpy as np
a = np.min(weight_data["weight"])-5
b = np.max(weight_data["weight"])+5
x = np.arange(a,b,0.01)
y = norm.pdf(x,loc=weight_mu,scale=weight_std)
plt.plot(x,y,lw=3,color="r")