
import cv2
import numpy as np



def purpleBox(img):
        
        blueImg, greenImg, redImg = cv2.split(img)
        
        blueMin = 150
        blueMax = 220

        redMin = 50
        redMax = 130

        greenMin = 70
        greenMax = 130
        
        # 160 = Red, 32 = Green, 240 = Blue
        
        (thresh, blueImg) = cv2.threshold(blueImg, blueMin, blueMax, cv2.THRESH_BINARY)
        (thresh, redImg) = cv2.threshold(redImg, redMin, redMax, cv2.THRESH_BINARY)
        (thresh, greenImg) = cv2.threshold(greenImg, greenMin, greenMax, cv2.THRESH_BINARY)

        #change this to be a bitwise AND of the above images using cv2.bitwise_and
        threshImg = cv2.bitwise_and(blueImg, cv2.bitwise_and(redImg, greenImg)) 
        
        




        edged = cv2.Canny(threshImg, 30, 200)
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
                        cv2.drawContours(img, [box], 0, (0,255,0), 2)

        
 
        return img, threshImg

        





