import cv2

cap = cv2.VideoCapture(0)

#global variables-Intially
center = (0,0)
clicked = False

#callback function

def draw_circle(event, x, y, flags, param):
    global center, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked=False #to draw circle when up
    if event == cv2.EVENT_LBUTTONUP:
        clicked=True

#connecting to window and function
cv2.namedWindow('Drawing_circle')
cv2.setMouseCallback('Drawing_circle', draw_circle)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if clicked:
        #true then drawing circle
        cv2.circle(frame, center=center, radius=50, color=(255,0,0), thickness=5)
    cv2.imshow('Drawing_circle', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
