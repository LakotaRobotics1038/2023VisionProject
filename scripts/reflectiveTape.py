
import cv2
import numpy as np


#cap = cv2.VidoeCapture(0)
tag1 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag1.jpeg")

tag2 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag2.jpeg")

tag3 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag3.jpeg")

tag4 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag4.jpeg")

tags = [tag1, tag2, tag3, tag4]

num = 0
for T in tags:
    T = cv2.resize(T , (300, 413))
    num = num + 1
    cv2.imshow(str(num ), T)
cv2.waitKey()






