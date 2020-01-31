import RPi.GPIO as GPIO
import time
import sys
import os
from logging import getLogger, INFO, DEBUG
logger = getLogger(__name__)


class Motor:
    def __init__(self, leftPin, rightPin):
        logger.debug("left={}, right={}".format(leftPin, rightPin))
        if GPIO.getmode() == None:
            GPIO.setmode(GPIO.BCM)
        self.leftPin = leftPin
        self.rightPin = rightPin
        GPIO.setup(self.leftPin, GPIO.OUT)
        GPIO.setup(self.rightPin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def turn(self, direct):
        if direct:
            logger.debug("Left turn {} {}".format(self.leftPin, self.rightPin))
            GPIO.output(self.leftPin, GPIO.HIGH)
            GPIO.output(self.rightPin, GPIO.LOW)
        else:
            logger.debug("Right turn {} {}".format(self.leftPin, self.rightPin))
            GPIO.output(self.leftPin, GPIO.LOW)
            GPIO.output(self.rightPin, GPIO.HIGH)

        time.sleep(0.3)
        GPIO.output(self.leftPin, GPIO.LOW)
        GPIO.output(self.rightPin, GPIO.LOW)
            

if __name__ == '__main__':
    logger.setLevel(DEBUG)
    signal = [True, False]
    m = Motor(27, 22)
    
    for i in range(5):
        for b in signal:
            m.turn(b)
            time.sleep(0.3)
    
