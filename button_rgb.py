from board import Board
from rgb_class import RGB
from button_class import Button
from time import sleep

rpi = Board()
button = Button(rpi, 24)
rgb = RGB(rpi, 16, 20, 21)

while True:
        if button.pressed:
            rgb.turnRed_on()
            sleep(0.1)
            rgb.turnGreen_on()
            sleep(0.1)
            rgb.turnBlue_on()
            sleep(0.1)
        elif button.pressed:
            rgb.turnRGB_off()
rpi.GPIO.cleanup()
