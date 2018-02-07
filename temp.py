import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
img1=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)

height, width = img.shape[:2]
temp=0

a=[[1/9,2/9,1/9],[2/9,4/9,2,9],[1/9,2/9,1/9]]
for x in range(-1,height-2):
    for y in range(-1,width-2):
        temp=0
        for i in range(x,x+9):
            for j in range(y,y+9):
                if(i>-1 and i<height and j>-1 and j<width ):
                    temp+=img[i,j]
        img1[x+1,y+1]=temp/9

plt.imshow(img1,cmap=plt.cm.Greys_r)
plt.show()
