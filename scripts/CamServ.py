from flask import Flask, Response
import cv2
from yoloProcess import process
from networktables import NetworkTables
import threading
import json

app = Flask(__name__)
cam = cv2.VideoCapture(0)

#default port for network tables = 1735

# init network tables

NetworkTables.initialize(server='172.16.185.112') #10.10.38.2 use later

# get custom table
tables = NetworkTables.getTable('Vision')




#valuesOut = table.getStringTopic('values').publish()
def run_network():
    while True:
        on = tables.getBoolean('on', True)
        print('running')
        if on:
            ret, img = cam.read()
            if ret:
                img, vals = process(img)
                print(vals)
                tables.putString('values', json.dumps(vals))


def get_image():
    while True:
        ret, img = cam.read()
        
        _, frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

@app.route('/stream')
def stream():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')

t = threading.Thread(target=run_network)
t.start()
app.run(host='0.0.0.0', port = 1180, threaded=True)









