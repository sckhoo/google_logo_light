import utime
import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# dim
tm.brightness(5)

tm.write([0, 0, 0, 0])
utime.sleep(2)

# 1234
tm.write([0x06, 0x5B, 0x4F, 0x66])
utime.sleep(2)

# 1.234
tm.write([0x06 | 128, 0x5B, 0x4F, 0x66])
utime.sleep(2)
# 12.34
tm.write([0x06, 0x5B | 128, 0x4F, 0x66])
utime.sleep(2)
# 123.4
tm.write([0x06, 0x5B, 0x4F | 128, 0x66])
utime.sleep(2)
# help
tm.show('help')