import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
height, width = img.shape[:2]
img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
plt.imshow(img,cmap=plt.cm.Greys_r)
plt.show()
