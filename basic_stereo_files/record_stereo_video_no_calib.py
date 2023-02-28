import cv2
import numpy as np

# initialize the camera capture objects for the left and right cameras
left_camera = cv2.VideoCapture(0)
right_camera = cv2.VideoCapture(1)

# set the capture properties
frame_width = int(left_camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(left_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(left_camera.get(cv2.CAP_PROP_FPS))

# create the VideoWriter object to store the video in mp4 format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width * 2, frame_height))

# start capturing frames from both the left and right cameras
while True:
    ret1, left_frame = left_camera.read()
    ret2, right_frame = right_camera.read()
    if not ret1 or not ret2:
        break
    
    # combine the left and right frames into a single stereo frame
    stereo_frame = np.concatenate((left_frame, right_frame), axis=1)
    
    # write the stereo frame to the output video
    output_video.write(stereo_frame)
    
    cv2.imshow('Stereo video', stereo_frame)
    if cv2.waitKey(1) == ord('q'):
        break

# release the camera capture objects and the VideoWriter object
left_camera.release()
right_camera.release()
output_video.release()
cv2.destroyAllWindows()
