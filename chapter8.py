import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(approx)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

            if obCor ==3: ObjectType = "Tri"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and asRatio <1.05: ObjectType = "Square"
                else: ObjectType = "Reactangle"
            elif objCor >4: ObjectType = "Circle"
            else: ObjectType = "None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.puttext(imgContour,ObjectType,(x+(w/2)-10,y+(h/2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
path = 'Resources/dog.jpg'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

cv2.imshow('Original', img)
cv2.imshow('Contours', imgContour)
cv2.waitKey(0)