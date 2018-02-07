import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/coins.png',0)
dst=cv2.imread('E:/WALLPAPERS/coins.png',0)

h, w=img.shape[:2]
plt.subplot(2,1,1)
plt.axis("off")
plt.title('Original Image')
plt.imshow(img,cmap=plt.cm.Greys_r)

for i in range(1,h-1):
    for j in range(1,w-1):
        a=[0]*9
        x=0
        for m in range(0,3):
            for n in range(0,3):
                a[x]=img[i-1+m][j-1+n]
                x=x+1
        a.sort()
        img[i][j]=a[5]
            
plt.subplot(2,1,2)
plt.axis("off")
plt.title('Median Image')
plt.imshow(dst,cmap=plt.cm.Greys_r)
plt.show()
