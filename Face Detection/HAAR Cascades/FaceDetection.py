import cv2
import numpy as np

#starting camera

cap = cv2.VideoCapture(0)

face_cascades = cv2.CascadeClassifier('Data/haarcascades/haarcascade_frontalface_default.xml')

eye_cascades = cv2.CascadeClassifier('Data/haarcascades/haarcascade_eye.xml')

def adj_detect_face(img):
    face_img = img.copy()
    face_rects = face_cascades.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
    
    eye_rects = eye_cascades.detectMultiScale(face_img, scaleFactor=1.1, minNeighbors=7)
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w, y+h), (255, 255, 255), 10)
        
    for (xe,ye,we,he) in eye_rects:
        cv2.rectangle(face_img, (xe,ye), (xe+we, ye+he), (0, 100, 100), 4)
    
    return face_img
    
while True:
    ret, frame = cap.read(0)
    frame = adj_detect_face(frame) # continously detecting face
    cv2.imshow('Video Face Detect', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release() #releasing camera
cv2.destroyAllWindows()