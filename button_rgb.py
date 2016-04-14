from board import Board
from rgb_class import RGB
from button_class import Button

rpi = Board()
button = Button(rpi, 24)
rgb = RGB(rpi, 16, 20, 21)

while True:
        if button.pressed:
            rgb.turnRed_on()
rpi.GPIO.cleanup()
