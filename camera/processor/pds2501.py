import RPi.GPIO as GPIO
import time
import sys

class PDS2501:
  __init__(self, dutyPin):
    GPIO.setup(dutyPin, GPIO.OUT)
    self.servo = GPIO.RWM(dutyPin, 50)
    self.servo.start(0)

  __del__(self):
    self.servo.stop()

  turn(self, duty):
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)

