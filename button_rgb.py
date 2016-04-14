from board import Board
from rgb_class import RGB
from button_class import Button

rpi = Board()
button = Button(rpi, 24)

while True:
        if button.pressed:
            print('Button Pressed')
            button.pressed = False
rpi.GPIO.cleanup()
