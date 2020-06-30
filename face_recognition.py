import cv2
import numpy as np
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainingData.yml')
faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")
Id=0
cam = cv2.VideoCapture(0)
while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        id=recognizer.predict(gray[y:y+h,x:x+w])
        if(id==9):
                Id="hrithik"
        elif(id==3):
                Id="A"
        else:
            Id="Unknown"
        cv2.rectangle(img, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(img, str(Id), (x,y-40), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,255), 3)
        cv2.imshow('Image',img)
    if(cv2.waitKey(10)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()