import cv2
import CamServ
import time


runCam = False
running = True


while running:
  

  key = cv2.waitKey(1)

  if key == ord('b'):
    runCam = True
    runCam = app.run(host='0.0.0.0', port = 1180, threaded=True)

  elif key == ord('n'):
    runCam = False
    app.stop(host='0.0.0.0', port = 1180, threaded=True)

  elif key == ord('q'):
    running = False 

  
  endTime2 = time.time()

camera.stop
