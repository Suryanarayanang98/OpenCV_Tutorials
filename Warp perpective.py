import cv2
import numpy as np

img=cv2.imread('cards.png')

width,height=250,350   # Standard poker card size

pts1=np.float32([[1780,220],[3000,580],[1260,1980],[2459,2326]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Outout",imgOutput)
cv2.waitKey(0)
