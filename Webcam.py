import cv2

cap=cv2.VideoCapture(0)

cap.set(3,640)   # Width3 is the id for the widthh
cap.set(4,480)   #Height 4 is id for the height
cap.set(10,100)  #Brightness 10 is the id for brightness

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

