from flask import Flask, Response
import cv2
from yoloProcess import process
from networktables import NetworkTables
from datetime import datetime
import threading
import json
import os

app = Flask(__name__)
cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)
serverAddr = '10.10.38.2'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
# init network tables
NetworkTables.initialize(server=serverAddr) #10.10.38.2 use later

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


def get_image():
    ret, img = cam1.read()
    ret, img = cam0.read()
# default port for network tables = 1735

    while True:
        shouldStream0 = tables.getBoolean('shouldStream0', True)

        if (shouldStream0):
            ret, img = cam0.read()
        else:
            ret, img = cam1.read()
        img = cv2.resize(img, (160, 120))
        _, frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

def record_cam():
    isRecording = False

    while True:
        ct = datetime.now()
        shouldRecord = tables.getBoolean('recording', False)
        if shouldRecord:
              ret0, img0 = cam0.read()
              ret1, img1 = cam1.read()
              if not isRecording:
                  # matchId = fmsTable.getNumber('MatchNumber', 0)
                  # rematchId = fmsTable.getNumber('ReplayNumber', 0)
                  # out = cv2.VideoWriter(str(matchId) + '-' + str(rematchId) + '.avi', fourcc, 60.0, (img.shape[1], img.shape[0]))
                  if ret0:
                      out0 = cv2.VideoWriter(f'{os.path.expanduser('~')}/Videos/{ct.strftime('%Y-%m-%d at %H-%M-%S')} cam0.avi', fourcc, 15.0, (img0.shape[1], img0.shape[0]))
                  if ret1:
                      out1 = cv2.VideoWriter(f'{os.path.expanduser('~')}/Videos/{ct.strftime('%Y-%m-%d at %H-%M-%S')} cam1.avi', fourcc, 15.0, (img1.shape[1], img1.shape[0]))
              if ret0:
                  out0.write(img0)
              if ret1:
                  out1.write(img1)
              isRecording = True
        elif isRecording and not shouldRecord:
            if out0:
                out0.release()
            if out1:
                out1.release()
            isRecording = False

@app.route('/stream')
def stream0():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')

recordingThread = threading.Thread(target=record_cam)
visionThread = threading.Thread(target=run_network)
visionThread.start()
recordingThread.start()
app.run(host='0.0.0.0', port = 1180, threaded=True)
