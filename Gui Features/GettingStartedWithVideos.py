#Importing libraries
import cv2
import numpy as np

#cv2.VideoCapture: To capture live stream with camera
#Its argument can be either the device index or the name of a video file.
#If a video file would like to be played, the camera index(0) is changed with the video file name
cap = cv2.VideoCapture(0)

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#Saving a video

cap = cv2.VideoCapture()

#Define the codec and create VideoWrite object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        #write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break

#Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
