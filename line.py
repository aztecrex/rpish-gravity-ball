from sense_hat import SenseHat
sense = SenseHat()

def plot(x,y):
    if x < 7 and x >= 0 and y < 7 and y >= 0:
       sense.set_pixel(x, y, 0, 255, 0)

def plot_line(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)

    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
#        swapped = True

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        if is_steep:
            plot(y, x)
        else:
            plot(x, y)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx


