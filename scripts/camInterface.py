import numpy as np
import cv2
import time
import requests
import threading
from threading import Thread, Event, ThreadError
from enum import Enum
from networktables import NetworkTables
import collections


class Cam():
    def __init__(self, url):
        self.stream = requests.get(url, stream=True)
        self.thread_cancelled = False
        self.thread = Thread(target=slef.run)
        print("camera initialised")

        self._resize_image_width = 320.0
        self._resize_image_height = 240.0

        
    def is_running(self):
        return self.thread.isAlive()

    def shut_down(self):
        self.thread_cancelled = True
        while self.thread.isAlive():
            time.sleep(1)
        return True


    @staticmethod
    def __resize_image(input, width, height):
        return cv2.resize(input, ((int)(width)), ((int)(height)), 0,0)



if __name__ == "__main__":
    url = 'https://localhost:11180/?action=stream'
    cam = Cam(url)

    cam.start()
