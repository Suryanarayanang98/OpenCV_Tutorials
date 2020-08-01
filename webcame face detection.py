import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade.load('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

cap.set(3,640)   # Width3 is the id for the widthh
cap.set(4,480)   #Height 4 is id for the height
cap.set(10,50)  #Brightness 10 is the id for brightness

while True:
    success,img=cap.read()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(imgGray,1.1,4) # image,scale,neighbors
    eyes=eye_cascade.detectMultiScale(imgGray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    for (x,y,w,h) in eyes:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),1)
        
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
    



#cv2.imshow("Output",img)
#cv2.waitKey(0)
