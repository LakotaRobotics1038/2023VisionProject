
import cv2
import numpy as np


def reflectiveTFilter(img):
        # Converting image to greyscale
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Converting greyscale image to binary (black or white)
        (thresh, grayImg) = cv2.threshold(grayImg, 212, 220,cv2.THRESH_BINARY)
        
        edged = cv2.Canny(grayImg, 30, 200)
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #cv2.(img, contours, -1, (0,220,0), 3)
        
        # Creating array to store top left point of each contour
        points = []
        for c in contours:
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                
                # Variables representing each corner of the contour
                bottomLeft = box[0]
                bottomRight = box[1]
                topRight = box[2]
                topLeft = box[3]
                
                # Solving area of contour
                distH = np.linalg.norm(bottomLeft - bottomRight)
                distV = np.linalg.norm(topRight - bottomRight)
                area = distH * distV
                
                if area <= 25000 and area >= 5000:
                        # Storing top left points in points array
                        points.append(topLeft)
                        
                        # Drawing contours around areas which are within the size limit and which reflect light
                        cv2.drawContours(img, [box], 0, (0,255,0), 2)

        
 
        return grayImg, points
        





