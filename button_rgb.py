from board import Board
from rgb_class import RGB
from button_class import Button
from time import sleep

rpi = Board()
button = Button(rpi, 24)
rgb = RGB(rpi, 16, 20, 21)

try:
    while True:
        if button.pressed:
            rgb.turnRed_on()
            rgb.turnRGB_off()
            button.pressed = False
            sleep(0.1)
        elif button.pressed:
            rgb.turnGreen_on()
            rgb.turnRGB_off()
            button.pressed = False
            sleep(0.1)
        elif button.pressed:
            rgb.turnBlue_on()
            rgb.turnRGB_off()
            button.pressed = False
            sleep(0.1)
        
except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    rpi.GPIO.cleanup()
