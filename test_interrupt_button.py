from machine import Pin
from time import sleep

#button20 = Pin(20, Pin.IN, Pin.PULL_DOWN)
#button21 = Pin(21, Pin.IN, Pin.PULL_DOWN)
#button22 = Pin(22, Pin.IN, Pin.PULL_DOWN)
button20 = Pin(20, Pin.IN, Pin.PULL_UP)
button21 = Pin(21, Pin.IN, Pin.PULL_UP)
button22 = Pin(22, Pin.IN, Pin.PULL_UP)
led=Pin(26,Pin.OUT)

def print20(change):
    print("Button 20")

def print21(change):
    print("Button 21")
    
def print22(change):
    print("Button 22")

button20.irq(handler=print20, trigger=Pin.IRQ_FALLING)
button21.irq(handler=print21, trigger=Pin.IRQ_FALLING)
button22.irq(handler=print22, trigger=Pin.IRQ_FALLING)

while True:
    led.toggle()            #Set led turn on
    sleep(0.25)
    print('.')