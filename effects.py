import numpy as np
import cv2

cap = cv2.VideoCapture('Splash - 23011.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('F','M','P','4')
out = cv2.VideoWriter('Boats.avi', fourcc, 30, (1920, 1080))
counter = 0
increase = True

while(cap.isOpened()):
    if counter == 255:
        increase = False
    ret, frame = cap.read()
    if ret==True:
        try:
            #frame = cv2.resize(frame, None, fx=.5, fy=.5)
            frame += counter
        except TypeError:
            break
        out.write(frame)
        if increase:
            counter += 1
        else:
            counter -= 1
        cv2.imshow('flower', frame)
        if cv2.waitKey(15) == 27:
            break
    else:
        break
	    
cap.release()
out.release()
cv2.destroyAllWindows()
