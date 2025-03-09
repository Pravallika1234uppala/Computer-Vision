import cv2
import os
import time
#frames are read fastely by camera(20frames per second) - to bring it back as video actually is

# assigning file path
path_video = "Output/MyCameravideo.mp4"

if not os.path.exists(path_video):
    print("ERROR: FILE NOT FOUND OR OPENED OR WRONG CODEC USED PLEASE CHECK!")
    exit()

cap = cv2.VideoCapture(path_video)
#this loads video file

if cap.isOpened() == False: #file not opened
    print("ERROR: FILE NOT FOUND OR OPENED OR WRONG CODEC USED PLEASE CHECK!")

while cap.isOpened():
    ret, frame = cap.read()
    #now frame has all the images from cap that has video captured object
    time.sleep(1/20)
    if ret == True: #if there are frames to return:
        #writing delay of 1/20
        cv2.imshow('My Saved Video', frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    else: #no frames to return
        break
cap.release()
cv2.destroyAllWindows()