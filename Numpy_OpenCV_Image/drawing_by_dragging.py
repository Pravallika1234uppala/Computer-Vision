import cv2
import numpy as np

#global parameters:

drawing = False #intially
ix=-1
iy=-1

############
##FUNCTION##
###########

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        #will start drwaing
        drawing=True
        ix,iy=x,y #coordinates of mouse(where button is pressed down)
    if event == cv2.EVENT_MOUSEMOVE:
        #dragging mouse-still drawing (expanding)
        if drawing == True:
            #drawing from click space to cxurrenrt location
            cv2.rectangle(img, (ix,iy), (x,y), (100,200,40),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        #no longer drawing
        drawing=False
        #just finish touch
        cv2.rectangle(img, (ix,iy),(x,y), (100,200,40),1)

###################
##SHOWING IMAGE####
###################

img = cv2.imread('Data/00-puppy.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#################################
###connecting window to function#
#################################

cv2.namedWindow(winname="drag&drop")

cv2.setMouseCallback("drag&drop", draw_rectangle)

while True:
    cv2.imshow("drag&drop", img)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()