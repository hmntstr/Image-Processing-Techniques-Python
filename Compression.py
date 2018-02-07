import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
tempss=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
#cv2.imwrite('E:/WALLPAPERS/beautiful-black-horse-pictures-real.jpg',temps)
plt.imshow(temps,cmap=plt.cm.Greys_r)
plt.imsave('E:/WALLPAPERS/beautiful-black-horse-pictures-real.jpg',temps, cmap=plt.cm.Greys_r)
c=1
height, width = temps.shape[:2]
temp=temps
for x in range(0, height):
    for y in range(0, width):
        s='{0:08b}'.format(temp[x,y])
        val=0
        for i in range(0,4):
            if s[i]=='1':
                val=val+np.power(2,3-i)
        temp[x,y]=val

#cv2.imwrite('E:/WALLPAPERS/beautiful-black-horse-pictures-compressed.jpg',temp)
plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.imsave('E:/WALLPAPERS/beautiful-black-horse-pictures-compressed.jpg',temp, cmap=plt.cm.Greys_r)
plt.show()
