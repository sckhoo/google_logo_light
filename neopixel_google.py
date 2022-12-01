from neopixel import Neopixel
import utime

def google_logo():
    numpix = 16
    strip = Neopixel(numpix, 0, 16, "RGB")
    seg1 = (255, 150, 0)
    seg2 = (255, 0, 0)
    seg3 = (0, 0, 255)
    seg4 = (0, 255, 0)
    strip.brightness(50)
    blank = (0,0,0)

    for i in range(numpix):
        strip.set_pixel(i, blank)
        strip.show()
    utime.sleep(1)  
    strip.set_pixel(0, seg1)
    strip.set_pixel(1, seg1)
    strip.set_pixel(2, seg1)
    strip.set_pixel(3, seg1)
    strip.set_pixel(4, seg2)
    strip.set_pixel(5, seg2)
    strip.set_pixel(6, seg2)
    strip.set_pixel(7, seg2)
    strip.set_pixel(8, seg3)
    strip.set_pixel(9, seg3)
    strip.set_pixel(10, seg3)
    strip.set_pixel(11, seg3)
    strip.set_pixel(12, seg4)
    strip.set_pixel(13, seg4)
    strip.set_pixel(14, seg4)
    strip.set_pixel(15, seg4)
    strip.show()

#google_logo()