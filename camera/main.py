from flask import Flask, render_template, Response
from processor.qr_detector import QRDetector as VideoCamera

from processor.mcp3208 import mcp3208
from processor.pds2501 import PDS2501
import RPi.GPIO as GPIO
import time
import threading

video_camera = VideoCamera(flip=False)

GPIO.setmode(GPIO.BCM)

# Servo motor GPIO 
SERVO_OUT = 12
servo = PDS2501(SERVO_OUT)

# AD convertor
CS = 8
CLK = 11
IN = 9
OUT = 10

adc = MCP3208(CS, CLK, IN, OUT)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def gen(camera):
  while True:
    # Draw picture
    frame = camera.get_frame()
    yield (b'--frame\r\n'
         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    # Entrance sensing
    entrDIst = adc.getData(0)
    exitDist = adc.getData(1)

    qrDetect = enterDist

    print("getting data:{}".format(camera.data))
    if(camera.data == b'qrcode'):
       print("open")
    else:
       print("close")

@app.route('/video_feed')
def video_feed():
  return Response(gen(video_camera),
          mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False, threaded=True)
