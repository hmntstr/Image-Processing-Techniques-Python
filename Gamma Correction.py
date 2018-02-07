import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/coins.png',0)

c=1
height, width = temps.shape[:2]
temp=temps
for x in range(0, height):
    for y in range(0, width):
        temp[x,y]=c*np.power(temp[x,y],0.8)

plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()

print(temp)
temp=cv2.imread('E:/WALLPAPERS/coins.png',0)
for x in range(0, height):
    for y in range(0, width):
        temp[x,y]=c*np.power(temp[x,y],1.2)%256
plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()

