from machine import I2C, Pin
from urtc import DS1307
import utime

i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
print(i2c.scan())

rtc = DS1307(i2c)

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    utime.sleep(1)
    print(rtc.datetime())
