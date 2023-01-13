from picamera2 import Picamera2, Preview
from time import sleep

camera = Picamera2()

camera_config = camera.create_preview_configuration()
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.configure(camera_config)
camera.start_preview(Preview.QTGL)
camera.start()
sleep(5)
