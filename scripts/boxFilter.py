
import cv2
import numpy as np



def purpleBox(img):
        
        blueImg = img[0]
        redImg = img[2]
        greenImg = img[1]
        
        
        # 160 = Red, 32 = Green, 240 = Blue
        
        (thresh, blueImg) = cv2.threshold(blueImg, 230, 250, cv2.THRESH_BINARY)
        (thresh, redImg) = cv2.threshold(redImg, 150, 170, cv2.THRESH_BINARY)
        (thresh, greenImg) = cv2.threshold(greenImg, 22, 42, cv2.THRESH_BINARY)
        
        return blueImg, redImg, greenImg



"""
        edged = cv2.Canny(grayImg, 30, 200)
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #cv2.(img, contours, -1, (0,220,0), 3)
        for c in contours:
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(img, [box], 0, (0,255,0), 2)
                
                bottomLeft = box[0]
                bottomRight = box[1]
                topRight = box[2]
                topLeft = box[3]
                distH = np.linalg.norm(bottomLeft - bottomRight)
                distV = np.linalg.norm(topRight - bottomRight)

                area = distH * distV
                
                if area <= 25000 and area >= 5000:
                        points.append(topLeft)
                        cv2.drawContours(img, [box], 0, (0,255,0), 2)

        
 
        return img, grayImg
"""
        





