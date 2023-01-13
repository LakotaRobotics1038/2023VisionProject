import cv2
from picamera2 import Picamera2
from reflectiveTape import reflectiveTFilter
from boxFilter import purpleBox


camera = Picamera2()
camera.start()

while True:
    img = camera.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    #fImg, points = reflectiveTFilter(img)
    blueImg, redImg, greenImg = purpleBox(img)
    cv2.imshow("blue", blueImg)
    cv2.imshow("greenWIN", greenImg)
    cv2.imshow("redIMG", redImg)
    cv2.imshow("img", img)
    print(img.shape)
    cv2.waitKey(1)
