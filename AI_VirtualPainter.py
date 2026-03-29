import cv2
import numpy as np
import time
import os
import HandTrackingMod as htm

# Load header images
folderPath = "Header"
myList = os.listdir(folderPath)

overlaylist = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlaylist.append(image)

header = overlaylist[0]

drawColor = (255, 0, 255)
brushThickness = 20
eraserThickness = 50

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.Detector(detectionCon=0.85)

xp, yp = 0, 0

success, img = cap.read()
img = cv2.flip(img, 1)
h, w, c = img.shape
canvas = np.zeros((h, w, 3), np.uint8)

lastClearTime = 0
cooldown = 1  # seconds

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findhands(img)
    lmlist = detector.findposition(img, draw=False)

    if len(lmlist) != 0:

        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()
        currentTime = time.time()

        if fingers == [1,1,1,1,1]:
            if currentTime - lastClearTime > cooldown:
                canvas = np.zeros((h, w, 3), np.uint8)
                lastClearTime = currentTime

        elif fingers[1] and fingers[2]:
            xp, yp = 0, 0

            if y1 < 125:
                if 250 < x1 < 450:
                    drawColor = (255, 0, 255)
                    header = overlaylist[0]
                elif 450 < x1 < 650:
                    drawColor = (255, 0, 0)
                    header = overlaylist[1]
                elif 650 < x1 < 850:
                    drawColor = (0, 255, 0)
                    header = overlaylist[2]
                elif 850 < x1 < 1050:
                    drawColor = (0, 0, 0)
                    header = overlaylist[3]

            cv2.rectangle(img, (x1, y1-15), (x2, y2+15), drawColor, cv2.FILLED)

        elif fingers[1] and fingers[2] == False:

            cv2.circle(img, (x1, y1), brushThickness//2, drawColor, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(canvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(canvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    imgGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, canvas)

    header = cv2.resize(header, (img.shape[1], 125))
    img[0:125, 0:img.shape[1]] = header

    cv2.imshow("Virtual Painter", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"MyDrawing_{int(time.time())}.png"
        cv2.imwrite(filename, canvas)
        print(f"Saved as {filename}")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()