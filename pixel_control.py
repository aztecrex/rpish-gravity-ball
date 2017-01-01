from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from line import plot_line

x = 3
y = 3
next_x = x;
next_y = y;

sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    global next_y
    if event.action != ACTION_RELEASED:
        next_y = clamp(y - 1)

def pushed_down(event):
    global y
    global next_y
    if event.action != ACTION_RELEASED:
       next_y = clamp(y + 1)

def pushed_left(event):
    global x
    global next_x
    if event.action != ACTION_RELEASED:
        next_x = clamp(x - 1)

def pushed_right(event):
    global x
    global next_x
    if event.action != ACTION_RELEASED:
        next_x = clamp(x + 1)

def draw():
    sense.clear()
    plot_line(0,0,x,y)
    plot_line(0,7,x,y)
    plot_line(7,0,x,y)
    plot_line(7,7,x,y)
    sense.set_pixel(x, y, 255, 255, 255)
  

def refresh():
    global x
    global next_x
    global y
    global next_y
    if x != next_x or y != next_y:
      x = next_x
      y = next_y
      draw();

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
draw()
pause()

