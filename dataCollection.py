import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

folder = 'images/y'
counter = 0

while True:
    success, img = cap.read()

    #detect the hand in video feed
    hands, img = detector.findHands(img)

    #crop the image to show the hands in seperate window
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        # 300x300 with 3 color channels
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

        #crop the image to show the hand and a buffer
        imgCrop = img[y-offset:y + h + offset, x-offset: x + w + offset]

        #Resize and center the img
        aspectRatio = h/w
        if aspectRatio > 1:
            k = imgSize/h
            wCalc = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop,(wCalc, imgSize))
            imgResizeShape = imgResize.shape
            wGap =  math.ceil((imgSize-wCalc)/2)
            imgWhite[:, wGap:wCalc+wGap] = imgResize
        else:
            k = imgSize/w
            hCalc = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop,(imgSize, hCalc))
            imgResizeShape = imgResize.shape
            hGap =  math.ceil((imgSize-hCalc)/2)
            imgWhite[hGap:hCalc+hGap, :] = imgResize

        #show image on window
        cv2.imshow('ImageWhite', imgWhite)
    else:
        cv2.putText(img, "No hand detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Image',img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/image_{time.time()}.jpg', imgWhite)
        print(counter)