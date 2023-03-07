import numpy as np
import cv2
from yoloProcess import process

cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

while(True):
	ret, frame = cam.read()
	ret2, frame2 = cam2.read()

	frame = process(frame)

	cv2.imshow('window', frame)
	cv2.imshow('window2', frame2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
#cv2.destroyallWindows()
