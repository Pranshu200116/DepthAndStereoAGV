import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('images/stereoCaliRectLeft/CRimageL0.png',0)
imgR = cv2.imread('images/stereoCaliRectRight/CRimageR0.png',0)

stereo = cv2.StereoBM_create(numDisparities=48, blockSize=15)
disparity = stereo.compute(imgL,imgR)

print(type(disparity))
plt.imshow(disparity)
plt.axis('off')
plt.show()

