import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L)

while True:
    ret, frame = cap.read()
    if ret: 
        cv2.imshow("win", frame)
    cv2.waitKey(1)


