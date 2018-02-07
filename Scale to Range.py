import numpy as np
import cv2
import matplotlib.pyplot as plt
temp=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)


height, width = temp.shape[:2]
z=temp.min()
for x in range(0, height):
    for y in range(0, width):
        temp[x,y]=temp[x,y]-z
        
z=temp.max()
K=255
for x in range(0, height):
    for y in range(0, width):
        temp[x,y]=K*(temp[x,y])/z

plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()
