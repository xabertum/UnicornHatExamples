import time
import unicornhat as unicorn

width, height = unicorn.get_shape()

for y in range (height):
  for x in range (width):
    if x == y:
      unicorn.set_pixel(x,y,255,5,255)
      unicorn.show()
      time.sleep(0.5)

for y in range (height):
  for x in range (width):
    if y + x == width - 1:
      unicorn.set_pixel(x,y,255,5,255)
      unicorn.show()
      time.sleep(0.5)
