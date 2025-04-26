import cv2

#function to select tracker based on input
#using choice variable
def askfortracker():
    print("Welcome! To continue, What Tracking API is used")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for MEDIANFLOW: ")
    choice = input("Please select your tracker: ")
    if choice == '0':
        tracker = cv2.legacy.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.legacy.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.legacy.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.legacy.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    return tracker
    

tracker = askfortracker()

if tracker is None:
    exit()

tracker_name = str(tracker).split()[1][11:]


#read video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

#reading first frame:
ret, frame = cap.read()

if not ret:
    print("Failed to read from camera. Exiting.")
    cap.release()
    exit()

print("Please select the ROI (press ENTER or SPACE to confirm, ESC to cancel)...")
cv2.imshow("Select ROI", frame)
cv2.waitKey(1)  
roi = cv2.selectROI("Select ROI", frame, False)
cv2.destroyWindow("Select ROI")

#to draw desired roi(region of interest) - manual

if roi == (0, 0, 0, 0):
    print("ROI selection canceled. Exiting.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

#intializing tracker with first frame and bounding box
ret = tracker.init(frame, roi)

while True:
    #reading new frame:
    ret, frame = cap.read()
    if not ret:
        break

    #updating tracker - for new frame
    success, roi = tracker.update(frame)
    #roi - tuple with 4 floats
    #getting them as integer values
    (x,y,w,h) = tuple(map(int, roi))

    #drawing rectangle if tracker moves
    if success:
        #if frame is moved or updated
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)

    else:
        #if frame not moved
        cv2.putText(frame, "Failure to detect tracking !!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    #tracker type on frame
    cv2.putText(frame, tracker_name, (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    #displaying result
    cv2.imshow(tracker_name, frame)

    #exit if pressed esc
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
