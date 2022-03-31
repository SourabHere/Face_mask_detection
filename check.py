from tkinter import Image
from black import out
import cv2
from cv2 import VideoCapture
from keras import models
from keras.models import load_model
import numpy as np
from PIL import Image 

model=load_model('mask.h5')

face_cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extract(img):
    face=face_cas.detectMultiScale(img,1.3,5)

    if face == ():
        return None

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cropped_face=img[y:y+h,x:x+w]

    return cropped_face

vid=cv2.VideoCapture(0)
while True:
    __,frame=vid.read()

    faces=face_extract(frame)
    if type(faces) is np.ndarray:
        faces=cv2.resize(faces,(200,200))
        im=Image.fromarray(faces,'RGB')

        img_arr=np.array(im)

        img_arr=np.expand_dims(img_arr,axis=0)
        img_arr=np.vstack([img_arr])
        pred=model.predict(img_arr)
        pred=np.argmax(pred)
        output=""

        if pred==0:
            output="with mask"
        elif pred==1:
            output="without mask"

        print(output)

        cv2.putText(frame,output,(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

        cv2.imshow('Vid',frame)

        if cv2.waitKey(1) & 0xff ==ord('q'):
            break
            vid.release()
            cv2.destroyAllWindows()