import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/tiger.jpg',1)
img1=cv2.imread('E:/WALLPAPERS/tiger.jpg',1)

b,g,r=cv2.split(img)
b1,g1,r1=cv2.split(img1)
height, width = img.shape[:2]
temp=0
for x in range(-1,height-2):
    for y in range(-1,width-2):
        temp=0
        for i in range(x,x+9):
            for j in range(y,y+9):
                if(i>-1 and i<height and j>-1 and j<width ):
                    temp+=b[i,j]
        b1[x+1,y+1]=temp/9

for x in range(-1,height-2):
    for y in range(-1,width-2):
        temp=0
        for i in range(x,x+9):
            for j in range(y,y+9):
                if(i>-1 and i<height and j>-1 and j<width ):
                    temp+=g[i,j]
        g1[x+1,y+1]=temp/9

for x in range(-1,height-2):
    for y in range(-1,width-2):
        temp=0
        for i in range(x,x+9):
            for j in range(y,y+9):
                if(i>-1 and i<height and j>-1 and j<width ):
                    temp+=r[i,j]
        r1[x+1,y+1]=temp/9
        
img1=cv2.merge((b1,g1,r1))
cv2.imshow('image',img1)
cv2.waitKey(0)
