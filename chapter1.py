import cv2
#image
img = cv2.imread("Resources/dog.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)
#videoCapture
cap = cv2.VideoCapture("path")
while True:
   success, img = cap.read()
   cv2.imshow("video", img)
   if cv2.waitKey(1) & 0xFF == ord("q"):
       break
#webcam
cap = cv2.VideoCapture(0)
cap.set(2,640)
cap.set(4,480)
while True:
   success, img = cap.read()
   cv2.imshow("video", img)
   if cv2.waitKey(1) & 0xFF == ord("q"):
       break
