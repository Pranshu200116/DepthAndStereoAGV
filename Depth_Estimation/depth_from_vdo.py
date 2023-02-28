import cv2
import numpy as np


# Load the video
video = cv2.VideoCapture("C:\\Users\\prans\\Documents\\vs code general\\output.avi")

# Create a StereoBM object for depth map calculation
stereo = cv2.StereoBM_create(numDisparities=48, blockSize=5)

# Loop through the frames in the video
while True:
    # Read the next frame from the video
    ret, frame = video.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Split the frame into left and right images
    height, width = frame.shape[:2]
    half_width = width // 2
    left_img = frame[:, :half_width]
    right_img = frame[:, half_width:]

    # Convert the images to grayscale
    left_gray = cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)

    # Compute the disparity map
    disparity = stereo.compute(left_gray, right_gray)

    # Normalize the disparity map for display
    cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Convert the disparity map to an RGB image for display
    disparity_rgb = cv2.applyColorMap(disparity.astype(np.uint8), cv2.COLORMAP_JET)

    # Display the disparity map
    cv2.imshow("Disparity Map", disparity_rgb)

    # Check for user input to exit
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video and close the window
video.release()
cv2.destroyAllWindows()
