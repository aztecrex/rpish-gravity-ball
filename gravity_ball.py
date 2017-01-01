from sense_hat import SenseHat
import math
import time

sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def next(v,gv):
  if gv < 0:
    return v - 1
  elif gv > 0:
    return v + 1
  else:
    return v

sense.clear()
x = 3
y = 3
while True:
    accel = sense.get_accelerometer_raw()
    next_x = clamp(next(x, accel['x']))
    next_y = clamp(next(y, accel['y']));
    sense.set_pixel(next_x,next_y,255,255,255)
    if next_x != x or next_y != y:
      sense.set_pixel(x,y,0,0,0)
    x = next_x;
    y = next_y;
    time.sleep(.15)


