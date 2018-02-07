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

ax=np.zeros((3,3), dtype=np.float)
ax[0][0]=-1
ax[0][1]=-2
ax[0][2]=-1
ax[2][0]=1
ax[2][1]=2
ax[2][2]=1
dst1=cv2.filter2D(img,-1,ax)

ay=np.zeros((3,3), dtype=np.float)
ay[0][0]=-1
ay[1][0]=-2
ay[2][0]=-1
ay[0][0]=1
ay[1][1]=2
ay[2][2]=1
dst2=cv2.filter2D(img,-1,ay)

dst=(dst1+dst2)%256

axarr[0, 1].plot(x,y)
axarr[0, 1].axis("off")
axarr[0, 1].set_title('Sobel Operator')
axarr[0, 1].imshow(dst,cmap=plt.cm.Greys_r)

bx=np.zeros((2,2), dtype=np.float)
bx[0][0]=-1
bx[1][1]=1
dst3=cv2.filter2D(img,-1,bx)

by=np.zeros((2,2), dtype=np.float)
by[0][1]=-1
by[1][0]=1
dst4=cv2.filter2D(img,-1,by)

dstf=(dst3+dst4)%256

axarr[1, 0].plot(x,y)
axarr[1, 0].axis("off")
axarr[1, 0].set_title('Robert Cross Operator')
axarr[1, 0].imshow(dstf,cmap=plt.cm.Greys_r)

axarr[1, 1].axis("off")

plt.show()
