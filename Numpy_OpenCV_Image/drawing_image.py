#1. Connecting Functions using a callback to an actual image


import cv2
import numpy as np



######################
######FUNCTION########
######################

#event function
def draw_circle(event, x, y, flags, param): #lot params are passed by default like x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img, center=(x,y), radius=25, color=(200,50,70),thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img=img, center=(x,y), radius=25, color=(100,250,90),thickness=-1)

#connected name window-opencv window name (connecting function to window)
cv2.namedWindow(winname='my_drawing')

#connecting setMouse Callback to window and function(just passing-so no parenthesis, no execution)
cv2.setMouseCallback('my_drawing', draw_circle)




###########################
######SHOWING IMAGE########
###########################


#image:
img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow('my_drawing', img) #showing image on window
    if cv2.waitKey(20) & 0xFF==27: #esc to exit
        break
cv2.destroyAllWindows()