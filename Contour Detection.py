import cv2
import numpy as np

def getContours(img):
                            #(image,retrival method-retrives extreme contours, Approximation
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    print(len(contours))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area:
            
                           #Image on which contour will be shown,contour,index,color,thickness
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            
            # Circumference
            peri = cv2.arcLength(cnt,True) # Contour, Closed?
            print("Perimeter",peri)

            # Number of corner points

            approx=cv2.approxPolyDP(cnt,0.01*peri,True)
            print("Corner",len(approx))

            # Create a bounding box around shapes

            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,h+y),(0,255,0),2)

            #Identfying the Shapes

            #if len(approx)==3:
            cv2.putText(imgContour,f"{len(approx)}",(x+10,y+10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
            cv2.imshow("Contour",imgContour)

        
 
img=cv2.imread('shape.jpg')
img=cv2.resize(img,(640,480))
img=img[:445,:]
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

cv2.imshow("ImgGray",imgGray)
cv2.imshow('Output',img)
cv2.imshow("Canny",imgCanny)
cv2.imshow('ImgBlur',imgBlur)
cv2.waitKey(0)
