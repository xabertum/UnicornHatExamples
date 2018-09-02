import unicornhat as unicorn
import time as time
import atexit
import colorsys

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.7)
width,height = unicorn.get_shape()


unicorn.set_pixel(4,0,255,255,255)
unicorn.show()
time.sleep(2)

unicorn.set_pixel(0,4,255,0,255)
unicorn.show()
time.sleep(2)

unicorn.set_pixel(4,7,255,0,0)
unicorn.show()
time.sleep(2)

unicorn.set_pixel(7,4,255,0,0)
unicorn.show()
time.sleep(2)
unicorn.clear()

time.sleep(4)
