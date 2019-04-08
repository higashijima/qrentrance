import RPi.GPIO as GPIO
import time
import sys

class PDS2501:
  def __init__(self, dutyPin):
    self.dutyPin = dutyPin

  def __del__(self):
    GPIO.cleanup()

  def turn(self, duty):
    GPIO.setup(self.dutyPin, GPIO.OUT)
    self.servo = GPIO.PWM(self.dutyPin, 50)
    self.servo.start(0)
    self.servo.ChangeDutyCycle(duty)
    print("DutyCycle:{}".format(duty))
    time.sleep(0.5)
    self.servo.stop()
    GPIO.cleanup(self.dutyPin)

