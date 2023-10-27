import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

classifier = Classifier('Model/keras_model.h5', 'Model/labels.txt')

imgSize = 300
offset = 20
folder = "image/"
counter_A = 0
counter_B = 0
counter_C = 0

labels = ['A', 'B', 'C']

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands , img = detector.findHands(img, draw=False)
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
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize , hCal))
            hGap = math.ceil((imgSize-hCal)/2)
            imageResizeShape = imgResize.shape
            imgWhite[hGap:hGap+hCal, 0:imageResizeShape[1]] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)


        cv2.putText(imgOutput,labels[index], (x,y-20), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2)
        cv2.rectangle(imgOutput, (x,y) , (x+w , y+h) , (255,0,255) , 3)

        # cv2.imshow('ImageCrop', imgCrop)
        # cv2.imshow('imgWhite', imgWhite)

    cv2.imshow("Image", imgOutput)
    key = cv2.waitKey(10)

