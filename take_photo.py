import cv2, os
import numpy as np
import pandas as pd
from PIL import Image

CSV_NAME = 'users.csv'
sample_num = 100 #Numero de Imagenes que seran tomadas y analizadas

def create_dataset():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    person_name = input('Dame tu nombre> ')
    Id = str(get_id_from_csv(name=person_name))

    sampleNum = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x, y),(x+w,y+h),(255,0,0),2)
            sampleNum = sampleNum + 1

            cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('Creando dataset', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif sampleNum > sample_num:
            break

    cam.release()
    cv2.destroyAllWindows()

def get_id_from_csv(name):
    try:
        users_data = pd.read_csv(CSV_NAME)
    except FileNotFoundError:
        users_data = pd.DataFrame({'Id':[1], 'name': [name]})
        new_user_id = 1
    else:
        new_user_id = users_data.count()["name"] + 1
        new_user = pd.DataFrame({"Id": [new_user_id], "name": [name]})
        users_data = pd.concat([users_data, new_user])
        print(users_data)

    users_data.to_csv(CSV_NAME,
                        columns=["Id", "name"],index=False)

    return new_user_id

def recognize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    cam = cv2.VideoCapture(0)
    isIdentifyed = False

    font = cv2.FONT_HERSHEY_SIMPLEX
    users = pd.read_csv(CSV_NAME)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im,(x, y),(x+w, y+h),(225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf<50):
                found_user = users[users.Id == Id]
                name="Buscando..."
                if found_user.name.any():
                    name = found_user.name.item()
            else:
                name="Buscando..."
            cv2.putText(im,str(name), org=(x,y+h),fontFace=font, color=(255,255,255), fontScale=1)
        cv2.imshow('im',im)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break


    cam.release()
    cv2.destroyAllWindows()

    return isIdentifyed