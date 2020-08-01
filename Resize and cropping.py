import cv2

img=cv2.imread('lambo.png')

# Getting the dimensions of our image
print(img.shape)    # Here it will display as (Height , Width, 3)

# Resizing
imgResize=cv2.resize(img,(640,480)) # Here it is (width,height) open-cv is weird
print(imgResize.shape)    # Here it will display as (Height , Width, 3)

# Cropping
imgCrop=img[200:400,200:1000] # Here it is again (Height,Width) since its numpy

cv2.imshow('crop',imgCrop)
cv2.imshow('Resize',imgResize)
cv2.imshow('Lambo',img)
cv2.waitKey(0)
