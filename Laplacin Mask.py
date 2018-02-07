import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/WALLPAPERS/coins.png',0)

x=np.linspace(0,2*np.pi,400)
y=np.sin(x**2)
f, axarr=plt.subplots(2,2)
axarr[0, 0].plot(x,y)
axarr[0, 0].axis("off")
axarr[0, 0].set_title('Original Image')
axarr[0, 0].imshow(img,cmap=plt.cm.Greys_r)

a=np.ones((3,3), dtype=np.float)
a[1][1]=-8


dst=cv2.filter2D(img,-1,a)
#cv2.imshow('Average Mask',dst)
#cv2.waitKey(0)

axarr[0, 1].plot(x,y)
axarr[0, 1].axis("off")
axarr[0, 1].set_title('Laplacian Image')
axarr[0, 1].imshow(dst,cmap=plt.cm.Greys_r)

dst1=255-dst

#dst1=cv2.filter2D(img,-1,a)
axarr[1, 0].plot(x,y)
axarr[1, 0].axis("off")
axarr[1, 0].set_title('Negative Laplacian')
axarr[1, 0].imshow(dst1,cmap=plt.cm.Greys_r)

sharped1=(dst+img)%256
axarr[1, 1].plot(x,y)
axarr[1, 1].axis("off")
axarr[1, 1].set_title('Sharpened Image')
axarr[1, 1].imshow(sharped1,cmap=plt.cm.Greys_r)

plt.show()
