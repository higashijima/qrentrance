from flask import Flask, render_template, Response
from processor.qr_detector import QRDetector as VideoCamera

import RPi.GPIO as GPIO
import time
import threading

video_camera = VideoCamera(flip=False)

GPIO.setmode(GPIO.BCM)

# Servo motor GPIO 
SERVO_OUT = 12
GPIO.setup(SERVO_OUT, GPIO.OUT)
servo = GPIO.PWM(SERVO_OUT, 50)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    if(camera.data == "qrcode"):
       servo.ChangeDutyCycle(2.5)
    else:
       servo.ChangeDutyCycle(7.25)

@app.route('/video_feed')
def video_feed():
  return Response(gen(video_camera),
          mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False, threaded=True)
