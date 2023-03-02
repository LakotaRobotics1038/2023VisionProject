from flask import Flask, Response
import cv2
from yoloProcess import process
import ntcore
import json

app = Flask(__name__)
cam = cv2.VideoCapture(0)

inst = ntcore.NetworkTableInstance.getDefault()
inst.startClient4('visionSystem')
inst.setServerTeam(1038)
table = inst.getTable('visionTable')
on = table.getBooleanTopic('on').subscribe(False)
valuesOut = table.getStringTopic('values').publish()




def get_image():
    while True:
        ret, img = cam.read()
        if ret and on.get():
            img, vals = process(img)
            valuesOut.set(json.dumps(vals))
        _, frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

@app.route('/stream')
def stream():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port = 1180, threaded=True)

#sleep(0.1)

#running = True

#runYolo = False

#while running:
 #   beg2Time = time.time()

  #  if runYolo:
   #     img = process(img)

        



