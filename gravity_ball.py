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

x = 3
y = 3
while True:
    sense.set_pixel(x,y)
    time.sleep(.1)
    accel = sense.get_accelerometer_raw()

    x = clamp(next(x, accel['x']))
    y = clamp(next(y, -1 * accel['y']));

    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)
