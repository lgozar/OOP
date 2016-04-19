from board import Board
from rgb_class import RGB
from button_class import Button
from time import sleep

rpi = Board()
button = Button(rpi, 24)
rgb = RGB(rpi, 16, 20, 21)

def switch(colour):
    
    if colour == 'red':
        rgb.turnRed_on()
        sleep(0.2)
        rgb.turnRGB_off()
    elif colour == 'green':
        rgb.turnGreen_on()
        sleep(0.2)
        rgb.turnRGB_off()
    elif colour == 'blue':
        rgb.turnBlue_on()
        sleep(0.2)
        rgb.turnRGB_off()
    else:
        rgb.turnRGB_Off()

try:
    while True:
        if button.pressed:
            rgb.turnRed_on()
            sleep(0.5)
            rgb.turnGreen_on()
            sleep(0.5)
            rgb.turnBlue_on()
            sleep(0.5)
            rgb.turnRGB_off()
            button.pressed = False
        
except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    rpi.GPIO.cleanup()
