import numpy as np
from matplotlib import pyplot as plt
import cv2
img=cv2.imread('E:/WALLPAPERS/coins_match.png',0)

cv2.imshow('abc',img)     
plt.hist(img.ravel(),256,[0,256])
plt.show()


height, width=img.shape[:2]
temp=img.ravel()

s=[0] * 256
sums=0
for x in range(0,temp.size):
    s[temp[x]]+=1

s1=[0] * 256
for x in range(0,256):
    for y in range(0,x):
        s1[x]+=s[y]
    s1[x]=255*s1[x]/temp.size

img=cv2.imread('E:/WALLPAPERS/coins.png',0)
for x in range(0,height):
    for y in range(0,width):
        for i in range(0,256):
            if s1[i]>=img[x,y]:
                img[x,y]=i
                break

cv2.imshow('abc',img)  
plt.hist(img.ravel(),256,[0,256])
plt.show()

