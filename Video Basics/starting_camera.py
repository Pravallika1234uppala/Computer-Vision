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
    cv2.imshow('Front Camera-Grey Mode',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    