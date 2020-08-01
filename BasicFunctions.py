import cv2
import numpy as np

img=cv2.imread('lena.png')

# Function to change the color and COLOR_BGR2GRAY tells it to change from rgb to gray
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Function to get a blur on the image
imgBlur=cv2.GaussianBlur(imgGray,(11,11),0)

# Edge Detection
imgCanny=cv2.Canny(img,150,200) # There are two thresholds.

# Dialation - This basically increases the thickness of the edges

kernel=np.ones((5,5),np.uint8) # Kernel is just a matrix
# Iteration controls how much thickness we want
imgDialate=cv2.dilate(imgCanny,kernel,iterations=1)

# Erosion - Opposite of dialation, decreases the thickness
imgErode=cv2.erode(imgDialate,kernel,iterations=1)

cv2.imshow('Erode',imgErode)
cv2.imshow('Dialate',imgDialate)
cv2.imshow('Canny',imgCanny)
cv2.imshow("blur",imgBlur)
cv2.imshow("gray",imgGray)
cv2.imshow("pic",img)
cv2.waitKey(0)
 
