# Import
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
imgSize = 300
offset = 20
folder = "image/"

# add more variable for more alphabet in prediction
counter_A = 0
counter_B = 0
counter_C = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize,imgSize,3) , np.uint8)*255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imageCropShape = imgCrop.shape
        aspectRatio = h/w
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize) )
            wGap = math.ceil((imgSize-wCal)/2)
            imageResizeShape = imgResize.shape
            imgWhite[0:imageResizeShape[0], wGap:wGap+wCal] = imgResize
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize , hCal))
            hGap = math.ceil((imgSize-hCal)/2)
            imageResizeShape = imgResize.shape
            imgWhite[hGap:hGap+hCal, 0:imageResizeShape[1]] = imgResize

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('imgWhite', imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(10)
    if key == ord('a'):
        counter_A += 1
        cv2.imwrite(f'{folder}/A/A_{counter_A}_Image_{time.time()}.jpg' , imgWhite)
        print(counter_A, " A images")
    if key == ord('b'):
        counter_B += 1
        cv2.imwrite(f'{folder}/B/B_{counter_B}_Image_{time.time()}.jpg' , imgWhite)
        print(counter_B, " B images")
    if key == ord('c'):
        counter_C += 1
        cv2.imwrite(f'{folder}/C/C_{counter_C}_Image_{time.time()}.jpg' , imgWhite)
        print(counter_C, " C images")

    # Copy and paste the above code for every latter you want