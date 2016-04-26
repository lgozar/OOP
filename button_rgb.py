from board import Board
from rgb_class import RGB
from button_class import Button
from time import sleep

rpi = Board()
button1 = Button(rpi, 24)
button2 = Button(rpi, 12)
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
        rgb.turnRGB_off()

try:
    while True:
        if button1.pressed:
            switch('red')
            switch('green')
            switch('blue')
            button1.pressed = False
        elif button2.pressed:
            switch('red')
            switch('green')
            switch('blue')
            button2.pressed = False
        
except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    rpi.GPIO.cleanup()
