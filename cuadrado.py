import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.7)
width, height = unicorn.get_shape()

for y in range(height):
  for x in range(width):
    unicorn.set_pixel(x,0,255,5,255)
    unicorn.show()
    time.sleep(0.05)

for y in range(height):
  for x in range(width):
    unicorn.set_pixel(7,y,255,5,255)
    unicorn.show()
    time.sleep(0.05)

for y in range(height):
  for x in range(width,0,-1):
    unicorn.set_pixel(x,7,255,5,255)
    unicorn.show()
    time.sleep(0.05)

for y in range(height,0,-1):
  for x in range(width):
    unicorn.set_pixel(0,y,255,5,255)
    unicorn.show()
    time.sleep(0.05)


