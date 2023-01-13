import cv2
from picamera2 import Picamera2
from reflectiveTape import reflectiveTFilter


camera = Picamera2()
camera.start()

while True:
    img = camera.capture_array()
    fImg, points = reflectiveTFilter(img)
    cv2.imshow("win", img)
    cv2.imshow("grayWIN", fImg)
    print(points)
    cv2.waitKey(1)
