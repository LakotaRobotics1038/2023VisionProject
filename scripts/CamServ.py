from flask import Flask, Response
import cv2
from yoloProcess import process
from networktables import NetworkTables
import threading
import json
import os

app = Flask(__name__)
cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
# init network tables
NetworkTables.initialize(server='10.10.38.2') #10.10.38.2 use later

# get custom table
tables = NetworkTables.getTable('Vision')
fmsTable = NetworkTables.getTable('FMSInfo')

def run_network():
    while True:
        on0 = tables.getBoolean('on0', False)
        on1 = tables.getBoolean('on1', False)
        ret = False
        if on0:
            ret, img = cam0.read()
        elif on1:
            ret, img = cam1.read()
        if ret:
            img, vals = process(img)
            print(vals)
            tables.putString('values', json.dumps(vals))


def get_image(camera):
    ret, img = cam1.read()
    ret, img = cam0.read()
    running = False
# default port for network tables = 1735

    while True:
        isCube = tables.getBoolean('shouldStream0', True)
        recording = tables.getBoolean('recording', False)
        if (isCube):
            ret, img = cam0.read()
        else:
            ret, img = cam1.read()
        if recording:
            if not running:
                matchId = fmsTable.getNumber('MatchNumber', 0)
                rematchId = fmsTable.getNumber('ReplayNumber', 0)
                out = cv2.VideoWriter(str(matchId) + '-' + str(rematchId) + '.avi', fourcc, 30.0, (img.shape[1], img.shape[0]))
            out.write(img)
            running = True
        elif running and not recording:
            out.release()
        img = cv2.resize(img, (160, 120))
        _, frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

@app.route('/stream')
def stream0():
    return Response(get_image(cam0), mimetype='multipart/x-mixed-replace; boundary=frame')

t = threading.Thread(target=run_network)
t.start()
app.run(host='0.0.0.0', port = 1180, threaded=True)









