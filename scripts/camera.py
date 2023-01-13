import cv2
from picamera2 import Picamera2
from reflectiveTape import reflectiveTFilter
from boxFilter import purpleBox
import time
from time import sleep
from yoloProcess import process


camera = Picamera2()
camera.start()

camera.brightness = 10
cv2.contrast = 100
camera.resolution = (1000, 600)
#cv2.resolution

sleep(0.1) 
running = True
while running:
    beg2Time = time.time()
      

    img = camera.capture_array()

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    
    img = process(img)

    
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == 113:
        print("stopping")
        running = False

    endTime2 = time.time()
    print('the whole program took ' + str(endTime2 - beg2Time))
    print(' ')
cv2.destroyAllWindows()
camera.stop()
