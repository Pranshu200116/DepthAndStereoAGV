import cv2


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

num = 0


while cap.isOpened():

    succes1, img0 = cap.read()
    succes2, img1 = cap2.read()


    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img0)
        cv2.imwrite('images/stereoRight/imageR' + str(num) + '.png', img1)
        print("images saved!")
        num += 1
        
    cv2.imshow('Img 1',img0)
    cv2.imshow('Img 2',img1)