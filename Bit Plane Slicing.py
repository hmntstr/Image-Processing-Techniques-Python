import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/coins.png',0)

c=1
height, width = temps.shape[:2]

for i in range(0,1):
    temp=cv2.imread('E:/WALLPAPERS/coins.png',0)
    for x in range(0, height):
        for y in range(0, width):
            s='{0:08b}'.format(temp[x,y])
            if s[i]=='1':
                temp[x,y]=np.power(2,7-i)
            else:
                temp[x,y]=0
                
        plt.subplot(121),plt.imshow(temp,cmap=plt.cm.Greys_r),plt.title(7-i)
        plt.xticks([]),plt.yticks([])

plt.show()
