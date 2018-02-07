import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)
temp=cv2.imread('E:/WALLPAPERS/beautiful-black-horse-pictures.jpg',0)

#temp[235][240]=178
#temp[800][400]=200
#temp[257][567]=60
#temp[60][100]=255

#temps=np.zeros((512,512),np.uint8)

font=cv2.FONT_HERSHEY_SIMPLEX
temp=cv2.putText(temp,'hemant',(100,500),font,5,(255,255),10)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(temps,cmap=plt.cm.Greys_r)

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Watermarked Image')
plt.imshow(temp,cmap=plt.cm.Greys_r)
plt.show()
