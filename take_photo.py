import cv2, os
import numpy as np
from PIL import Image

def create_dataset():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    Id = input('Dame un Id> ')
    sampleNum = 0
    print(cam)
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            print(x,y,w,h)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            sampleNum=sampleNum + 1
            cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('Creando dataset', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif sampleNum > 50:
            break

    cam.release()
    cv2.destroyAllWindows()


def recognize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    cam = cv2.VideoCapture(0)
    isIdentifyed = False

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im,(x, y),(x+w, y+h),(225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf<50):
                if(Id==1):
                    Id="Wildin"
                    isIdentifyed = True
                elif(Id==2):
                    Id="Profesor"
                    isIdentifyed = True
            else:
                Id="Buscando..."
            cv2.putText(im,str(Id), org=(x,y+h),fontFace=font, color=(255,255,255), fontScale=1)

            if isIdentifyed:
                break
        cv2.imshow('im',im)
        if isIdentifyed:
            break
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break


    cam.release()
    cv2.destroyAllWindows()

    return isIdentifyed


