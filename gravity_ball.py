from sense_hat import SenseHat
import math
import time

sense = SenseHat()

r = 255
g = 255
b = 255
old_x = 0
old_y = 0
def draw(x,y):
    sense.set_pixel(x,y,r,g,b)
    if old_x != x or old_y != y:
        sense.set_pixel(x, y,r, g, b)
    old_x = x;
    old_y = y;


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
    draw(next_x, next_y, x, y)
    time.sleep(.15)
