import cv2
from deepface import DeepFace
import numpy as np
#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#video= cv2.VideoCapture(0)
#video = cv2.VideoCapture(1, cv2.IMREAD_UNCHANGED)
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not cap.isOpened():
    print("cannot open camera")
    exit()
while (True):

     ret,frame = cap.read()
     if not ret:
        print("can't receive frame(stream end?). Exiting...")
        break

     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
     for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        try:
             analyze = DeepFace.analyze(frame,actions=['emotion'])
             emo = analyze['dominant_emotion']
            # emotion_labels = analyze['angry']
             if emo =='angry' or emo == 'sad':
                print(emo)
        except:
            print("no face")

   
   
     cv2.imshow('frame',gray)
     key=cv2.waitKey(1)
     if key==ord('q'):
     
      break
cap.release()
cv2.destroyAllWindows()

