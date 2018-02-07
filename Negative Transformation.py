import numpy as np
import cv2
import matplotlib.pyplot as plt
temp=cv2.imread('E:/WALLPAPERS/coins.png',0)


height, width = temp.shape[:2]
for x in range(0, height):
    for y in range(0, width):
        temp[x,y]=255-temp[x,y]

plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()
