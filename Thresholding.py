import numpy as np
import cv2
import matplotlib.pyplot as plt

temp=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)


height, width = temp.shape[:2]
for x in range(0, height):
    for y in range(0, width):
        if temp[x,y]<128:
            temp[x,y]=0
        elif temp[x,y]>128:
            temp[x,y]=255

plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()
