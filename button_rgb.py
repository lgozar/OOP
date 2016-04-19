from board import Board
from rgb_class import RGB
from button_class import Button
from time import sleep

rpi = Board()
button = Button(rpi, 24)
rgb = RGB(rpi, 16, 20, 21)

try:
    while True:
        if button.pressed == 1:
            rgb.turnRed_on()
            sleep(0.1)
        else:
            rgb.turnRGB_off()
            
        if button.pressed == 1:
            rgb.turnGreen_on()
            sleep(0.1)
            rgb.turnRGB_off()
        if button.pressed == 1:
            rgb.turnBlue_on()
            sleep(0.1)
            rgb.turnRGB_off()
            button.pressed = False
        
except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    rpi.GPIO.cleanup()
