#imports
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from sklearn.mixture import GaussianMixture
from matplotlib import pyplot

#reading in the data using the local path (change to 'ClusterPlot.csv' for other testing)
data = pd.read_csv(r'C:\Users\viswa\Documents\UTD\Sophomore\Fall\ACM Research\Coding-Challenge\ClusterPlot.csv')

#setting up the plot
plt.figure(figsize=(7,7))
plt.grid(zorder=0, color="lightgrey")
plt.scatter(data["V1"],data["V2"])

#gaussian mixture model for the 3 cluster variation
gmm1 = GaussianMixture(n_components=3)
gmm1.fit(data)

#gaussian prediction for 3 clusters
labels = gmm1.predict(data)
plt.scatter(data["V1"],data["V2"], c=labels, cmap='plasma')
plt.show()

#probability for the 3 cluster variation
p1 = gmm1.predict_proba(data)
print (p1)

#gaussian mixture model for the 2 cluster variation
gmm2 = GaussianMixture(n_components=2)
gmm2.fit(data)

#gaussian prediction for 2 clusters
labels = gmm2.predict(data)
plt.grid(zorder=0, color="lightgrey")
plt.scatter(data["V1"],data["V2"], c=labels, cmap='plasma')
plt.show()

#probability for the 2 cluster variation
p2 = gmm2.predict_proba(data)
print (p2)
