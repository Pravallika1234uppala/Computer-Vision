import cv2
img = cv2.imread('Data/00-puppy.jpg')
while True:
    cv2.imshow("Puppy", img)
    #if cv2.waitKey(10) & 0xFF==27:
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()