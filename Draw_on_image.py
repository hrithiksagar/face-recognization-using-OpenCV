import cv2
img=cv2.imread('himanshu.jpg')
cv2.line(img,(100,100),(300,100),(0,0,255),2)
cv2.rectangle(img,(100,200),(300,400),(255,255,0),2)
cv2.ellipse(img,(300,80),(80,20),30,255,90,(255),-1) #-for filled value
#cv2.rectangle(img,(100,200),(300,400),(255,255,0),-1)  for filled rectangle
cv2.putText(img,'himanshu',(100,220),cv2.FONT_HERSHEY_COMPLEX,5,(255,0,0),5,cv2.LINE_AA)#cv2 for smoothness in text
#cv2.imwrite('ss.jpg',img)
#cv2.imwrite('ssss.png',img)
cv2.imshow('',img)
cv2.waitKey(0)



import numpy as np
img2=cv2.imread('himanshu.jpg',cv2.IMREAD_COLOR)
pts=np.array([[10,5],[20,30],[70,20],[10,50],[70,5]],np.int32)
pts=pts.reshape((-1,1,2))
img2=cv2.polylines(img2,[pts],False,(0,0,255))
cv2.imshow('',img2)
cv2.waitKey(0)
