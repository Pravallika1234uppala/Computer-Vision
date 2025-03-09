import cv2
import os

#starting camera

cap = cv2.VideoCapture(0)

#height & width:(of frame)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#video-frame of images

# Ensure output directory exists
output_directory = "Output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
path_video = os.path.join(output_directory, "MyCameravideo.mp4")

writer_video = cv2.VideoWriter(path_video, cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))
#keeping it out of loop-destination and width and height is ready

while True:
    #reading frames of images
    ret, frame = cap.read()

    if not ret:
        break
    
    cv2.imshow('Front Camera-Grey Mode',frame)
    
    writer_video.write(frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

writer_video.release()
cap.release()
cv2.destroyAllWindows()

#this video is saved fast ( fast as computer reads)