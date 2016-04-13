from board import Board
import time

rpi = Board()

rpi.GPIO.setup(24, rpi.GPIO.IN, pull_up_down = rpi.GPIO.PUD_UP)

while True:
    input_state = rpi.GPIO.input(24)
    if input_state == False:
        print('Button Pressed')
        time.sleep(1)

