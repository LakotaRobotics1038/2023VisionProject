
import cv2
import numpy as np


"""tag1 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag1.jpeg")

tag2 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag2.jpeg")

tag3 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag3.jpeg")

tag4 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag4.jpeg")

tag5 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag5.jpeg")

tag6 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag6.jpeg")

tag7 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag7.jpeg")

tag8 = cv2.imread("/home/team1038/repos/2023VisionProject/data/AprilTag8.jpeg")

tags = [tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8]

num = 0
for T in tags:
    T = cv2.resize(T , (300, 413))
    num = num + 1
    cv2.imshow(str(num ), T)
cv2.waitKey()"""

Path = "/home/team1038/repos/2023VisionProject/data/AprilTag"

jp = ".jpeg"

for x in range(1,9):
    inputpath = Path +(str(x)) + jp
    image = cv2.imread(inputpath)
    image =  cv2.resize(image, (300, 413))
    cv2.imshow(str(x), image)
cv2.waitKey()






