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
    global old_x, old_y, r, g, b
    sense.set_pixel(x, y, r, g, b)
    if old_x != x or old_y != y:
        sense.set_pixel(old_x, old_y, 0, 0, 0)
    old_x = x;
    old_y = y;

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def next(v,gv):
    if gv < -0.12:
        return v - 1
    elif gv > 0.12:
        return v + 1
    else:
        return v

def pushed_up:
    g = clamp(g + 1, 0, 255)

def pushed_left:
    r = clamp(r + 1, 0, 255)

def pushed_right:
    r = clamp(b + 1, 0, 255)

def pushed_down:
    g = clamp(g - 1, 0, 255)
    r = clamp(r - 1, 0, 255)
    b = clamp(b - 1, 0, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

sense.clear()
x = 3
y = 3
draw(x, y)
while True:
    accel = sense.get_accelerometer_raw()
    gx, gy = accel['x'], accel['y']
    mag = math.sqrt(gx * gx + gy * gy)
    x = clamp(next(x, gx))
    y = clamp(next(y, gy));
    draw(x, y)
    mag = math.sqrt(gx * gx + gy * gy)
    amount = mag / .6
    adjust = .1 * amount
    time.sleep(.15 - adjust)
