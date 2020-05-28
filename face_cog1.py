
import numpy as np
import cv2
from PIL import Image
import os

cascadePath = '/home/pi/studyPython/haarcascades/haarcascade_frontalface_default.xml'
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('train.yml')
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'LYE', 'Luna', 'YeEun', 'Lee']

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


try:
    while True:
        ret, image = cam.read()
        image = cv2.flip(image,0) #상하 좌우 반전
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW),int(minH))
        )        

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y), (x+w,y+h),(255,0,0),2)
            roi_gray = gray [y:y+h, x:x+w]
            id, confidence = recognizer.predict(roi_gray)

            if(confidence <100):
                id = names[id]
                confidence = " {0}%".format(round(100-confidence))
            else:
                id = "unknown"
                confidence = " {0}%".format(round(100-confidence))
            
            cv2.putText(image,str(id),(x+5,y-5),font,1,(255,255,255),2)
            cv2.putText(image,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)


        cv2.imshow('video',image)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

finally:
    cam.release()
    cv2.destroyAllWindows()