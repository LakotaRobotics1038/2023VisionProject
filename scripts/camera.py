import cv2
from picamera2 import Picamera2
from reflectiveTape import reflectiveTFilter
from boxFilter import purpleBox
from time import sleep

camera = Picamera2()
camera.start()
camera.brightness = 10
cv2.contrast = 100
sleep(0.1) 
running = True
while running:
    img = camera.capture_array()
    #dont change convert line, below
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    #fImg, points = reflectiveTFilter(img)
    img, threshImg = purpleBox(img)
    cv2.imshow("img", img)
    cv2.imshow('threshImg', threshImg)

    if cv2.waitKey(1) == 113:
        print("stopping")
        running = False


cv2.destroyAllWindows()
camera.stop()
