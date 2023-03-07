import numpy as np
import cv2
import time
import requests
import threading
from threading import Thread, Event, ThreadError
from enum import Enum
from networktables import NetworkTables
import collections


#BoundingRectangle = collections.namedtuple('BoundingRectangle', 'x y w h')

class Cam():

  def __init__(self, url):
    
    self.stream = requests.get(url, stream=True)
    self.thread_cancelled = False
    self.thread = Thread(target=self.run)
    print "camera initialised"


    #self.__resize_image_width = 320.0
    #self.__resize_image_height = 240.0
    #self.__resize_image_interpolation = cv2.INTER_CUBIC

    #self.resize_image_output = None

    #self.__hsv_threshold_input = self.resize_image_output
   # """
    #The ideal Hue rangefor the block is 19-30.
    #The ideal hue range for the paper is 19-52, and Saturation is 7-227
    #"""
    #self.__hsv_threshold_hue = [19, 30]
    #self.__hsv_threshold_saturation = [7, 227]
    #self.__hsv_threshold_value = [112, 192]

    #self.hsv_threshold_output = None

    #self.__blur_input = self.hsv_threshold_output
    #self.__blur_type = BlurType.Median_Filter
    #self.__blur_radius = 35

    #self.blur_output = None

    #self.filterMask_output = None
    #self.calculatedBoundingRectangle = None
    
  def start(self):
    self.thread.start()
    print "camera stream started"
    Cam.createNetworkTable()
    print "Network Table created."
    
  def run(self):
    bytes=''
    skipper = 0
    while not self.thread_cancelled:
      try:
        bytes+=self.stream.raw.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
          skipper = skipper + 1
          jpg = bytes[a:b+2]
          bytes = bytes[b+2:]
          #CHANGED SKIPPER from 3 to 1; so it will run every 2nd frame
          if skipper > 3:
            skipper = 0
            #print "Process frame..."
            #NOTE: acquiring image through a different mechanism - previously it was from frame.array and we got frame from "frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)"
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
            cv2.imshow('cam',img)

            start = time.time()

            # Step Resize_Image0:
            #self.__resize_image_input = img
            #(self.resize_image_output) = self.__resize_image(self.__resize_image_input, self.__resize_image_width, self.__resize_image_height, self.__resize_image_interpolation)


            #Step convert image to HSV
            #self.__hsv_threshold_input = self.resize_image_output
            #(self.hsv_threshold_output) = self.__hsv_threshold(self.__hsv_threshold_input, self.__hsv_threshold_hue, self.__hsv_threshold_saturation, self.__hsv_threshold_value)


            #Step Blur image
            #self.__blur_input = self.hsv_threshold_output
            #(self.blur_output) = self.__blur(self.__blur_input, self.__blur_type, self.__blur_radius)
            #cv2.imshow('Frame3', self.blur_output)


            #Step FilterMask
            #self.filterMask_output = self.filterMask(self.blur_output)


            #step Find Bounding Rectangle
            #self.calculatedBoundingRectangle = self.findBoundingRectangle(self.filterMask_output)


            end = time.time()
            duration = end - start


            #Step Output To Network Table
            #if self.calculatedBoundingRectangle == None:
              #self.outputToNetworkTable('0', duration, '0')
            #else:
              #step calculate X coordinate (we use Y since it is rotated by 90 degrees)
              #boundingRectX = self.calculatedBoundingRectangle.x + (self.calculatedBoundingRectangle.w /2)
              #area = self.calculatedBoundingRectangle.h * self.calculatedBoundingRectangle.w
              #self.outputToNetworkTable(self.xToAngle(boundingRectX / self.__resize_image_width), duration, area)
              
            
          if cv2.waitKey(1) == 113:
            exit(0)

      except ThreadError:
        print "error"
        self.thread_cancelled = True
        
        
  def is_running(self):
    return self.thread.isAlive()
      
    
  def shut_down(self):
    self.thread_cancelled = True
    #block while waiting for thread to terminate
    while self.thread.isAlive():
      time.sleep(1)
    return True

  #@staticmethod
  #def xToAngle(inX):
    #result = (inX - 0.5) * 46
    #return str(round(result, 2))

  #For the horizontal angle (x-coordinate), negative means a turn to the left is required; a positive means a turn to the right is required
  #@staticmethod
  def outputToNetworkTable(xCoord, inDuration, inarea):
    #print 'NetTab ' + str(xCoord) + " " + str(round(1 / inDuration, 2))         
    sd = NetworkTables.getTable("SmartDashboard")
    #sd.putString('Angle', str(xCoord))
    #sd.putNumber('Area', float(inarea))
    if inDuration > 0:
      sd.putNumber('FPS',  str(round(1 / inDuration, 2)))
    return

  @staticmethod
  def deleteNetworkTableEntries():
    sd = NetworkTables.getTable("SmartDashboard")
    if sd.containsKey("x"):
      sd.delete("x")
    if sd.containsKey("y"):
      sd.delete("y")
    return

  #Initializes NetworkTables, which is on port 1735 by default
  @staticmethod        
  def createNetworkTable():
    NetworkTables.initialize()
    return    

  #Filter the mask to remove noise
  @staticmethod
  def filterMask(inImage):
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    maskOpen=cv2.morphologyEx(inImage,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    return maskClose

  #Find the contours in the image, and put a bounding rectangle around them
  @staticmethod
  def findBoundingRectangle(inImage):
    maskFinal = inImage
    image,contours,_=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    brX = 0
    brY = 0
    brW = 0
    brH = 0
    maxIndex = 0 # this tells the index of the contours of max area
    maxArea = -5
    for i in range(len(contours)):
      brX,brY,brW,brH=cv2.boundingRect(contours[i])
      if brW*brH > maxArea :
        maxArea = brW*brH
        maxPosition = i
      if len(contours) > 0:
        brX,brY,brW,brH=cv2.boundingRect(contours[maxIndex])
        boundRect = BoundingRectangle(x=brX, y=brY, w=brW, h=brH)
        return boundRect
      else:
        return None



  #@staticmethod
  #def __resize_image(input, width, height, interpolation):
    #return cv2.resize(input, ((int)(width), (int)(height)), 0, 0, interpolation)

  #@staticmethod
  #def __hsv_threshold(input, hue, sat, val):
    #out = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
    #return cv2.inRange(out, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

  #@staticmethod
  #def __blur(src, type, radius):
    #if(type is BlurType.Box_Blur):
     #ksize = int(2 * round(radius) + 1)
      #return cv2.blur(src, (ksize, ksize))
    #elif(type is BlurType.Gaussian_Blur):
      #ksize = int(6 * round(radius) + 1)
      #return cv2.GaussianBlur(src, (ksize, ksize), round(radius))
    #elif(type is BlurType.Median_Filter):
      #ksize = int(2 * round(radius) + 1)
      #return cv2.medianBlur(src, ksize)
    #else:
      #return cv2.bilateralFilter(src, -1, round(radius), round(radius))


#BlurType = Enum('BlurType', 'Box_Blur','Gaussian_Blur', 'Median_Filter', 'Bilateral_Filter')
    
if __name__ == "__main__":
  url = 'http://localhost:1180/?action=stream'
  cam = Cam(url)
  cam.start()
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
