#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

gData = list()

numthetas = 7
numts = 21

with open("gData.csv", 'r') as gf:
    for num in gf:
        gData.append(float(num.strip()))

gData = np.asarray(gData)
gData = np.reshape(gData,(numthetas,numts))

thetas = np.arange(numthetas)
ts = np.arange(numts)

thetaMat = list()
tMat = list()
for theta in thetas:
    thetaMat.append(theta * np.ones(numts))
    
    tMat.append(ts)

#thetaMat = np.transpose(thetaMat)
print(tMat)
print(thetaMat)
print(gData)
    


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

print(gData.shape)
print(ts.shape)
print(thetas.shape)
ax.plot_surface(tMat, thetaMat, gData)

plt.show()
