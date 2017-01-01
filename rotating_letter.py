from sense_hat import SenseHat

sense = SenseHat()

sense.show_letter("J", text_colour=[0, 0, 255], back_colour=[255, 128, 128])

while True:
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    z = sense.get_accelerometer_raw()['z']

    x = round(x, 0)
    y = round(y, 0)

    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)

