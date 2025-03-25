import cv2
import numpy as np
import matplotlib
from matplotlib import cm

road_img = cv2.imread('Data/road_image.jpg')
road_img_copy = np.copy(road_img)


marker_img = np.zeros(road_img.shape[:2], dtype=np.int32)

segments = np.zeros(road_img.shape, dtype=np.uint8)


def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)


colors = []

for i in range(10): #for 10 iterations
    colors.append(create_rgb(i))
    #for 10 created 10 colors list
  

###GLOBAL VARIABLES:####

n_markers = 10

#no. of marks for segments

current_marker = 1

#index position for list of colors-can be adjusted by user input

marks_updated = False

#if marks is updated or not 



#####CALL BACK FUNCTION####

def mouse_callback(event,x,y,flags,param):
    global marks_updated
    if event == cv2.EVENT_LBUTTONDOWN:
        #drawing circle- one for tracking matkers that is sent to watershed algorithm
        #and other for user's image
        cv2.circle(marker_img,(x,y),10,(current_marker),-1)
        cv2.circle(road_img_copy,(x,y),10,colors[current_marker],-1)
        marks_updated = True




#connectinf call back to window

cv2.namedWindow('Road Image')

cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    cv2.imshow('WaterShed Segments', segments)
    #black image
    cv2.imshow('Road Image', road_img_copy)
    #image user sees

    #closing windows
    
    k = cv2.waitKey(2)
    if k == ord('q'):
        break
    #to clear and start fresh
    elif k == ord('c'):
        road_img_copy=road_img.copy()
        marker_img = np.zeros(road_img.shape[:2], dtype=np.int32)
        segments = np.zeros(road_img.shape, dtype=np.uint8)
    
    elif k>0 and chr(k).isdigit():
        current_marker=int(chr(k))
        #if number is given then that color is taken for that segment

    #updating the markers
    if marks_updated:
        marker_img_copy = marker_img.copy()
        cv2.watershed(road_img, marker_img_copy)
        segments = np.zeros(road_img.shape, dtype=np.uint8)
        for color_index in range(n_markers):
            segments[marker_img_copy==(color_index)]=colors[color_index]
            #this colors segments

cv2.destroyAllWindows()