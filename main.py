from modules.mcp3208 import MCP3208
import RPi.GPIO as GPIO

RELAT_CTL = 18

def main():
  ADC = MCP3208(11, 10, 9, 8)
  GPIO.setup(RELAY_CTL, GPIO.OUT)
  while True:
    for ch in range(2):
      value = ADC.adc(ch)
      if vale < 2048:
        GPIO.output(RELAY_CTL, GPIO.HIGH)
      else:
        GPIO.output(RELAY_CTL, GPIO.LOW)
        
if __name__ == '__main__':
  main()

