import cv2
cap=cv2.VideoCapture('dataset/bahubali.mp4')
fc=cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
while(True):
    rtv,frame=cap.read()
    faces=fc.detectMultiScale(frame,1.2)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        print(x,y,w,h)
    cv2.imshow('title',frame)
    if( cv2.waitKey(10)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()