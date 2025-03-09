import cv2

#starting camera

cap = cv2.VideoCapture(0)

#height & width:(of frame)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#video-frame of images

while True:
    #reading frames of images
    ret, frame = cap.read()
    gray_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Front Camera-Grey Mode',gray_frames)
    if cv2.waitKey(3) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    