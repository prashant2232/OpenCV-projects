import cv2
import numpy as np

img = cv2.imread('Resources/dog.jpg')
kernel = np.ones((3,3),np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('imgGray', imgGray)
cv2.imshow('imgBlur', imgBlur)
cv2.imshow('imgCanny', imgCanny)
cv2.imshow('imgDialation', imgDialation)
cv2.imshow('imgErode', imgErode)
cv2.waitKey(0)