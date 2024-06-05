import cvzone
import cv2
import os
import math
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

menuImages = []
path = "filters"
pathList = os.listdir(path)

pathList.sort()

for x, pathImg in enumerate(pathList):
    img = (cv2.imread(path+"/"+pathImg, cv2.IMREAD_UNCHANGED))
    img = cv2.resize(img, (100, 100))
    menuImages.append(img)

menuCount = len(menuImages)

detector = HandDetector(detectionCon=0.8)


menuChoice = -1
dragImage = False

while True:
    success, cameraFeedImg = cap.read()
    cameraFeedImg = cv2.flip(cameraFeedImg, 1)

    wHeight, wWidth, wChannel = cameraFeedImg.shape
    x = 0
    y = 0
    xIncrement = math.floor(wWidth / menuCount)
    # Create yIncrement variable

    handsDetector = detector.findHands(cameraFeedImg, flipType=False)
    hands = handsDetector[0]
    cameraFeedImg = handsDetector[1]

    try:
        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            indexFingerTop = lmList1[8]
            indexFingerBottom = lmList1[6]

            if (indexFingerTop[1] < 100):
                i = 0
                while (xIncrement*i <= wWidth):
                    if (indexFingerTop[0] < xIncrement*i):
                        menuChoice = i-1
                        dragImage = True
                        break
                    i = i+1

            if (indexFingerTop[1] > indexFingerBottom[1]):
                dragImage = False

        if (dragImage):
            imgX = cv2.resize(menuImages[menuChoice], (0, 0), fx=1, fy=1)
            cameraFeedImg = cvzone.overlayPNG(
                cameraFeedImg, imgX, [int(indexFingerTop[0]), int(indexFingerTop[1])])

    except Exception as e:
        print(e)

    for image in menuImages:
        # Use value of y while displaying the image and keep x =0
        cameraFeedImg = cvzone.overlayPNG(cameraFeedImg, image, [x, 0])
        # Change the y location instead of the x location (increment y by yIncrement and subtract 4 from it)
        x = x + xIncrement

    cv2.imshow("Face Filter App", cameraFeedImg)
    cv2.waitKey(1)
