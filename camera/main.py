from flask import Flask, render_template, Response
from processor.qr_detector import QRDetector as VideoCamera

from processor.mcp3208 import MCP3208
from processor.motor import Motor
import RPi.GPIO as GPIO
import time
from datetime import datetime as dt
import threading

import os
from logging import getLogger, basicConfig, DEBUG, INFO
basicConfig(format="%(asctime)s:%(levelname)s:%(message)s:%(pathname)s:%(funcName)s(%(lineno)s)")
logger = getLogger(__name__)
if os.environ.get('DEBUG', None):
    logger.setLevel(DEBUG)
else:
    logger.setLevel(INFO)

video_camera = VideoCamera(flip=False)
GPIO.setmode(GPIO.BCM)

# motor GPIO 
LEFT = 27
RIGHT = 22
OPEN = True
CLOSE = False

# AD convertor
CS = 8
CLK = 11
IN = 9
OUT = 10

adc = MCP3208(CLK, OUT, IN, CS)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("begin")
    return render_template('index.html')

def dispWindow(camera):
    logger.info("begin")
    frame = camera.get_frame()
    yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen(camera):
    logger.info("begin")
    motor = Motor(LEFT, RIGHT)
    while True:
        # Draw picture
        #dispWindow(camera)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # Entrance sensing
        enterDist = adc.getData(0)
        exitDist = adc.getData(1)

        logger.debug("enterDist={}, exitDist={}, data={}".format(enterDist, exitDist, camera.get_data()))
#        qrDetect = enterDist < 2048
        qrDetect = True

        if(qrDetect):
            logger.debug("enter here")

            enterDt = dt.now()
            # wait for detecting QRcode until 3seconds 
            while(not camera.detected and (dt.now()-enterDt).seconds < 3):
                dispWindow(camera)
                logger.info("Enter any person:{}".format(camera.get_data()))
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
                if(camera.get_data() == b'qrcode'):
                    logger.info("open")
#                    motor.turn(OPEN)
                    time.sleep(1)
                    break

#                motor.turn(CLOSE)

@app.route('/video_feed')
def video_feed():
    logger.info("begin")
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
