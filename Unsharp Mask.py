import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/coins.png',0)

x=np.linspace(0,3*np.pi,400)
y=np.sin(x**3)
f, axarr=plt.subplots(3,2)
axarr[0, 0].plot(x,y)
axarr[0, 0].axis("off")
axarr[0, 0].set_title('Original Image')
axarr[0, 0].imshow(img,cmap=plt.cm.Greys_r)

a=np.ones((3,3), dtype=np.float)/9

dst=cv2.filter2D(img,-1,a)
#cv2.imshow('Average Mask',dst)
#cv2.waitKey(0)
axarr[0, 1].plot(x,y)
axarr[0, 1].axis("off")
axarr[0, 1].set_title('Mean Image')
axarr[0, 1].imshow(dst,cmap=plt.cm.Greys_r)

mask=(img-dst)%256
axarr[1, 0].plot(x,y)
axarr[1, 0].axis("off")
axarr[1, 0].set_title('Mask')
axarr[1, 0].imshow(mask,cmap=plt.cm.Greys_r)

unsharp=(img+mask)%256
axarr[1, 1].plot(x,y)
axarr[1, 1].axis("off")
axarr[1, 1].set_title('UnSharp Image')
axarr[1, 1].imshow(unsharp,cmap=plt.cm.Greys_r)

k=2
highboost=(img+k*mask)%256
axarr[2, 0].plot(x,y)
axarr[2, 0].axis("off")
axarr[2, 0].set_title('Highboosted Image')
axarr[2, 0].imshow(highboost,cmap=plt.cm.Greys_r)

axarr[2, 1].axis("off")
plt.show()
