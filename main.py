from neopixel_google import google_logo
from machine import I2C, Pin
from urtc import DS1307
import utime
import tm1637
from dht import DHT11, InvalidChecksum, InvalidPulseCount
import rp2
import network
import ubinascii
import urequests as requests
import time
from secrets import secrets
import socket
#import json
import io
import json

def setup_wifi():
    # Set country to avoid possible errors
    rp2.country('MY')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # See the MAC address in the wireless chip OTP
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print('mac = ' + mac)
    # Load login data from different file for safety reasons
    ssid = secrets['ssid']
    pw = secrets['pw']
    wlan.connect(ssid, pw)
    # Wait for connection with 10 second timeout
    timeout = 10
    while timeout > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        timeout -= 1
        print('Waiting for connection...')
        time.sleep(1)
    wlan_status = wlan.status()
    if wlan_status != 3:
        raise RuntimeError('Wi-Fi connection failed')
    else:
        print('Connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
        
#def check_wifi():
#    return 1

def setup_all_pin():
    global rtc, tm, button20, button21
    # Setup RTC
    #i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
    #rtc = DS1307(i2c)
    # Setup TM1637 - 4 digits 7-segment LED display
    tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
    # Setup DHT11
    # button
    button20 = Pin(20, Pin.IN, Pin.PULL_UP)
    button21 = Pin(21, Pin.IN, Pin.PULL_UP)

def get_googl():
    global lastClose
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=GOOGL&apikey=SF4RD6ZNU9C759O7'
    r = requests.get(url)
    data = r.json()
    lastDate = data["Meta Data"]["3. Last Refreshed"]
    lastClose = data["Time Series (Daily)"][lastDate]["4. close"]

def increment_display(change):
    global display
    if display < 3:
        display += 1
    else:
        display = 1 # supposed to be zero. RTC hardware failure. so, remove clock function

google_logo()
setup_all_pin()
led=Pin(26,Pin.OUT)
button20.irq(handler=increment_display, trigger=Pin.IRQ_FALLING)
button21.irq(handler=google_logo(), trigger=Pin.IRQ_FALLING)
sensor = DHT11(Pin(2, Pin.OUT, Pin.PULL_DOWN))
setup_wifi()
get_googl()
display = 1 # 0=clock, 1=temp, 2=hum, 3=GOOGL price
#utime.sleep(2)
old_humidity, old_temp = 70, 30

# main loop
while True:
    #(year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    #if minute == 0 and second <= 5 and check_wifi():
    #        print("get google price")
    #        get_googl()
    try:
        sensor.measure()
    except InvalidChecksum:
        sensor = DHT11(Pin(10, Pin.OUT, Pin.PULL_DOWN))
    except InvalidPulseCount:
        sensor = DHT11(Pin(10, Pin.OUT, Pin.PULL_DOWN))
    if display == 0:
        tm.numbers(hour, minute, True)
    elif display == 1:
        try:
            sensor.measure()
            temp = sensor.temperature
            old_temp = temp
        except InvalidChecksum:
            sensor = DHT11(Pin(10, Pin.OUT, Pin.PULL_DOWN))
        except InvalidPulseCount:
            sensor = DHT11(Pin(10, Pin.OUT, Pin.PULL_DOWN))
            temp = old_temp
        tm.temperature(int(temp))
    elif display == 2:
        try:
            humidity = sensor.humidity
            old_humidity = humidity
        except InvalidPulseCount:
            humidity = old_humidity
        tm.number(int(humidity))
    elif display == 3:
        tm.number(round(float(lastClose)))
    utime.sleep(0.5)
    led.toggle()
