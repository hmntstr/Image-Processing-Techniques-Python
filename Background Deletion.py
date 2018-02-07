import numpy as np
import cv2
import matplotlib.pyplot as plt
temps=cv2.imread('E:/WALLPAPERS/coins.png',0)
fgbg = cv2.BackgroundSubstractor()
temps = fgbg.apply(temps)
cv2.imshow('image',temps)
cv2.waitKey(0)
