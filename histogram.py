import numpy as np
from matplotlib import pyplot as plt
import cv2
img=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)

plt.hist(img.ravel(),256,[0,256])
plt.show()
