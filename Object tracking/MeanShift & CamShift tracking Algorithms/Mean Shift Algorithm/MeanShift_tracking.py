#grabbing image from camera

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

#Intial tracking window-using corner detection
#10 best corners detected-then tracking them
#(face tracking using object detection- to grab face location
#applying mean shift tracking on detected face-bunch of pixels)
#detecting face - one time and then tracking the pixels using mean

face_cascade = cv2.CascadeClassifier('Data/haarcascades/haarcascade_frontalface_default.xml')

face_rects = face_cascade.detectMultiScale(frame)
#numpy array where face is detected
#just grabbing the face -face it detected

#tuple
(face_x, face_y, w, h) = tuple(face_rects[0])

#face coordinates - first detected - size of a window
track_window = (face_x, face_y, w, h)

#region of interest - face on frame
roi = frame[face_y:face_y+h, face_x:face_x+w]

#hsv-rgb 2 hsv
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#color histogram
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0,180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#to find mean

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
#criteria paraameters

while True:
    ret, frame = cap.read()
    #to read more frames in loop
    if ret == True:
        #converting new frame to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #backpropagation to track the detected object(frame and region of interest color histogram
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        
        #to find mean by moving blue points
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        #rectangle - coordinates of track window
        x,y,w,h = track_window

        #to draw box for tracking window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 5)
        cv2.imshow('img', img2)

        k = cv2.waitKey(10)&0xFF
        if k == 27:
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()