import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((height/4,width/4),90,1)
img=cv2.warpAffine(img,M,(height,width))
plt.imshow(img,cmap=plt.cm.Greys_r)
plt.show()
