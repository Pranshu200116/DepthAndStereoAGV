import numpy as np
import cv2
from matplotlib import pyplot as plt

# Camera parameters to undistort and rectify images
cv_file = cv2.FileStorage()
cv_file.open('stereoMap.xml', cv2.FileStorage_READ)

stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()

# Open both cameras
cap_right = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap_left = cv2.VideoCapture(2,cv2.CAP_DSHOW)

num = 0

# set the capture properties
frame_width = int(cap_left.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_left.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30


# create the VideoWriter object to store the video in mp4 format
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output.avi', fourcc, fps , (frame_width * 2, frame_height))


while(cap_right.isOpened() and cap_left.isOpened()):

    #print(frame_height, frame_width, fps)

    succes_right, frame_right = cap_right.read()
    succes_left, frame_left = cap_left.read()
    # Undistort and rectify images
    frame_right = cv2.remap(frame_right, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    frame_left = cv2.remap(frame_left, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
                     
    # combine the left and right frames into a single stereo frame
    stereo_frame = np.concatenate((frame_left, frame_right), axis=1)

    # write the stereo frame to the output video
    output_video.write(stereo_frame)

    cv2.imshow('Stereo video', stereo_frame)
    if cv2.waitKey(1) == ord('q'):
        break
    

    '''

    # Show the frames
    cv2.imshow("frame right", frame_right) 
    cv2.imshow("frame left", frame_left)

    if k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoCaliRectLeft/CRimageL' + str(num) + '.png', frame_left)
        cv2.imwrite('images/stereoCaliRectRight/CRimageR' + str(num) + '.png', frame_right)
        print("images saved!")
        num += 1   

    

    # Hit "q" to close the window
    if k & 0xFF == ord('q'):
        break

    '''

# Release and destroy all windows before termination
cap_right.release()
cap_left.release()
output_video.release()
cv2.destroyAllWindows()