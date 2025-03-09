import cv2
cap = cv2.VideoCapture(0)
#starting camera

#global variables:(Intially)
pt1=(0,0)
pt2=(0,0)

topLeft_clicked = False
botRight_clicked = False

#call back function:
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if topLeft_clicked and botRight_clicked:
            #already drawed now need to reset
            pt1=(0,0)
            pt2=(0,0)
            topLeft_clicked=False
            botRight_clicked=False
            
        if topLeft_clicked==False:
            #need to set true if event happened
            pt1=(x,y)
            topLeft_clicked=True
            
        elif botRight_clicked==False:
            pt2=(x,y)
            botRight_clicked=True
            

#window naming
cv2.namedWindow('Drawing_Shape')

#connecting to call back:
cv2.setMouseCallback('Drawing_Shape', draw_rectangle)

while True:
    ret, frame = cap.read()
    
    #drawing a shape based on global variables:

    #if first click
    if topLeft_clicked:
        #drawing circle for points
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
        
    #if both first and second circle:
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)
        #drawing rectangle(final)
    cv2.imshow('Drawing_Shape', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()