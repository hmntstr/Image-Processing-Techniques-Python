import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/coins.png',0)

plt.subplot(2,1,1)
plt.axis("off")
plt.title('Original Image')
plt.imshow(img,cmap=plt.cm.Greys_r)

a=np.ones((3,3), dtype=np.float)
a[0][1]=2
a[1][0]=2
a[1][1]=4
a[1][2]=2
a[2][1]=2

a=a/16

dst=cv2.filter2D(img,-1,a)

plt.subplot(2,1,2)
plt.axis("off")
plt.title('Blurred Image')
plt.imshow(dst,cmap=plt.cm.Greys_r)
plt.show()
