import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)

c=1
height, width = temps.shape[:2]
temp=temps
for x in range(0, height):
    for y in range(0, width):
        if temp[x,y]>112 and temp[x,y]<146:
            temp[x,y]=200
        elif temp[x,y]<=112:
            temp[x,y]=0
        elif temp[x,y]>=146:
            temp[x,y]=255
plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()
