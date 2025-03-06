import cv2
#import matplotlib.pyplot as plt
#%matplotlib inline

def showimage(winname, img, width=400, height=400):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)  # To create resizable window instead of default
    cv2.resizeWindow(winname, width, height)  # Setting window size
    while True:
        cv2.imshow(winname, img)
        if cv2.waitKey(10) & 0xFF == ord('q'):  # 'q' to close
            break
    cv2.destroyAllWindows()
    
#reading image cv2 reads in bgr format
img_bgr = cv2.imread('Data/00-puppy.jpg')

showimage('ColorSpaces-BGR', img_bgr) #width and height if not passed are taken default.


#RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
showimage('ColorSpaces-RGB', img_rgb) #width and height if not passed are taken default.

#HSV-(hue Saturation Value)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
showimage('ColorSpaces-HSV', img_hsv) #width and height if not passed are taken default.


#HLS-(hue lightness Saturation)
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)
showimage('ColorSpaces-HLS', img_hls) #width and height if not passed are taken default.


        
cv2.destroyAllWindows()