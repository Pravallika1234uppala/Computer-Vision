import cv2

cap = cv2.VideoCapture(0)
#starts camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#width and height of camera

#Top left corner-cordiantes - To draw rectangle
x = width//2
y = height//2

#width & height of rectangle:(rectangle to draw)
w = width//4
h = height//4

#bottom right corner
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x,y), (x+w,y+h), color=(0,255,255), thickness=4)
    cv2.imshow('Video-Rectangle', frame)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()