import numpy as np
import cv2

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#Load the Image
imgo=cv2.imread('E:/WALLPAPERS/horse_picture.jpg')

height, width = imgo.shape[:2]

temp=cv2.GaussianBlur(imgo,(15,15),0)

#Create a mask holder
mask = np.zeros(imgo.shape[:2],np.uint8)

# newmask is the mask image I manually labelled
newmask = cv2.imread('E:/WALLPAPERS/horse_picture.jpg',0)
# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1

#Grab Cut the object
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#Hard Coding the Rect� The object must lie within this rect.
rect = (10,10,width-30,height-30)
cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img1 = imgo*mask[:,:,np.newaxis]

#Get the background
background = imgo-img1

#Change all pixels in the background that are not black to white
background[np.where((background > [0,0,0]).all(axis = 2))] = [255,255,255]

#Add the background and the image
final = background + img1

#To be done � Smoothening the edges�.


k = cv2.waitKey(0)

final=imgo-final
result=cv2.imread('E:/WALLPAPERS/horse_picture.jpg')
for x in range(0,3):
    for y in range(200,height-1):
        for z in range(100,width-20):
            if final[y][z][x]==0:
                result[y][z][x]=max(final[y-50][z][x],final[y-51][z][x],final[y-50][z+1][x],final[y-51][z+1][x])
                
cv2.imshow('image', result)
cv2.waitKey(0)
