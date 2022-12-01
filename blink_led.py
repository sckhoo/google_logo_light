from time import sleep
from machine import Pin
led=Pin(26,Pin.OUT)        #create LED object from pin13,Set Pin13 to output

while True:
  led.toggle()            #Set led turn on
  sleep(0.5)
  #print("blink")
