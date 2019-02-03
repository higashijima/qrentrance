from modules.mcp3208 import MCP3208

def main():
  ADC = MCP3208(11, 10, 9, 8)
  while True:
    for ch in range(2):
      value = ADC.adc(ch)
      print("{}:{}".format(ch, value))


if __name__ == '__main__':
  main()

