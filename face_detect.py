import cv2
img=cv2.imread('dataset/zac.jpg')
#img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceClassifier=cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
eyeClassifier=cv2.CascadeClassifier('dataset/haarcascade_eye.xml')
facelist = faceClassifier.detectMultiScale(img, 1.1)
i = 0
for x, y, w, h in facelist:
    i += 1
    crop_face = img[y:y + h, x:x + w]
    cv2.imwrite("face" + str(i) + ".jpg", crop_face)
for x, y, w, h in facelist:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    crop_face = img[y:y + h, x:x + w]
    eyes = eyeClassifier.detectMultiScale(crop_face)
    print(eyes)
    for ex, ey, ew, eh in eyes:
        i += 1
        ee = crop_face[ey:ey + eh, ex:ex + ew]
        cv2.imwrite(str(i) + ".jpg", ee)
        # cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('title', img)
cv2.waitKey(0)