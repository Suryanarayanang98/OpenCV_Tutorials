import cv2
import numpy as np

# Zero will make the picture Black
img=np.zeros((512,512,3)) # One Depth, so this will be grayscale
                          # So we will give depth 3 here

# Coloring A specific region of image
#img[200:312,200:312]=255,0,0  # B G R

#--- FOR Lines----
# Remember in cv its always (width,height)

cv2.line(img,(0,0),(300,300),(0,255,0),3) # Image,starting point,ending point,
                                          # color (here green), thickness(opt)

# ----For Rectangles----
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# If you want the rectangle to be filled with color
cv2.rectangle(img,(250,350),(img.shape[1],img.shape[0]),(255,0,0),cv2.FILLED)

# ---- For Circle----
cv2.circle(img,(400,50),30,(255,255,0),5) # image,centre, radius,color,thickenss

# ----For Text----
# (image,Text,Origin,Text Font,Scale,Color,thickness)
cv2.putText(img,"Hello OpenCV", (300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),2)

cv2.imshow('Image',img)
cv2.waitKey(0)
