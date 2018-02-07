import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/coins.png',0)

plt.subplot(2,1,1)
plt.axis("off")
plt.title('Original Image')
plt.imshow(img,cmap=plt.cm.Greys_r)

a=np.ones((3,3), dtype=np.float)/9

dst=cv2.filter2D(img,-1,a)
#cv2.imshow('Average Mask',dst)
#cv2.waitKey(0)
plt.subplot(2,1,2)
plt.axis("off")
plt.title('Blurred Image')
plt.imshow(dst,cmap=plt.cm.Greys_r)
plt.show()
