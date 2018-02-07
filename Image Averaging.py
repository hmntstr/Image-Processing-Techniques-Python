import numpy as np
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread('E:/WALLPAPERS/coins.png',0)

plt.subplot(2,1,1)
plt.axis("off")
plt.title('Original Image')
plt.imshow(img1,cmap=plt.cm.Greys_r)

img2=cv2.imread('E:/WALLPAPERS/coins.png',0)

result=(img1+img2)%256
plt.subplot(2,1,2)
plt.axis("off")
plt.title('Avergage Image')
plt.imshow(result,cmap=plt.cm.Greys_r)
plt.show()
