import cv2

# Initialize the stereo camera capture using cv2.VideoCapture()
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 
cap2 = cv2.VideoCapture(2, cv2.CAP_DSHOW) 

# Set the camera properties (such as frame size and exposure) if needed
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

# Camera parameters to undistort and rectify images
cv_file = cv2.FileStorage()
cv_file.open('stereoMap.xml', cv2.FileStorage_READ)

stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()


# Initialize the stereo block matching algorithm using cv2.StereoSGBM_create()
stereo = cv2.StereoSGBM_create(numDisparities=512, blockSize=125)

# Loop through the camera frames and convert them to a colorful depth map
while True:
    # Read the stereo camera frames using cv2.VideoCapture.read()
    retL, left_frame = cap.read()
    left_frame = cv2.resize(left_frame, (480,640))

    retR, right_frame = cap2.read()
    right_frame = cv2.resize(right_frame, (left_frame.shape[1],left_frame.shape[0]) )

    left_frame = cv2.remap(left_frame, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    right_frame = cv2.remap(right_frame, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)

    print(left_frame.shape)
    print(right_frame.shape)


    '''
    # Split the stereo frames into left and right images
    left_frame = frame[:, :frame.shape[1]//2]
    right_frame = frame[:, frame.shape[1]//2:]
    '''

    # Convert the left and right images to grayscale using cv2.cvtColor()
    left_gray = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)

    # Compute the depth map using cv2.StereoSGBM.compute()
    disp_map = stereo.compute(left_gray, right_gray)

    # Normalize and convert the depth map to a color image using cv2.applyColorMap()
    #disp_map_norm = cv2.normalize(disp_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #disp_map_color = cv2.applyColorMap(disp_map_norm, cv2.COLORMAP_JET)

    # Show the depth map in a window using cv2.imshow()
    cv2.imshow('Depth Map', disp_map)
    #cv2.imshow('Depth Map', disp_map_color)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera capture and close all windows using cv2.VideoCapture.release() and cv2.destroyAllWindows()
cap.release()
cap2.release()
cv2.destroyAllWindows()
