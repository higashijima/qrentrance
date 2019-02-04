import mcp3208
import RPi.GPIO as GPIO

RELAY_CTL = 12

def main():
  ADC = MCP3208(11, 10, 9, 8)
  GPIO.setup(RELAY_CTL, GPIO.OUT)
  while True:
    for ch in range(2):
      value = ADC.adc(ch)
      if value < 2048:
        GPIO.output(RELAY_CTL, GPIO.HIGH)
      else:
        GPIO.output(RELAY_CTL, GPIO.LOW)
      print("{}:{}".format(ch, value))

if __name__ == '__main__':
  main()
