from board import Board #import Board class
from rgb_class import RGB #import RGB class
from button_class import Button #import Button class
from time import sleep

rpi = Board() #implement Board class to variable rpi
button1 = Button(rpi, 24) #implement Button class to variable button1 with pin 24
button2 = Button(rpi, 12) #implement Button class to variable button2 with pin 12
rgb = RGB(rpi, 16, 20, 21) #implement RGB class to variable rgb with pins 16 20 21

def switch(colour): #a function to switch from different colors
    
    if colour == 'red': #turns red rgb on
        rgb.turnRed_on()
        sleep(0.2)
        rgb.turnRGB_off()
    elif colour == 'green': #turns green rgb on
        rgb.turnGreen_on()
        sleep(0.2)
        rgb.turnRGB_off()
    elif colour == 'blue': #turns blue rgb on
        rgb.turnBlue_on()
        sleep(0.2)
        rgb.turnRGB_off()
    else:
        rgb.turnRGB_off()

try:
    while True:
        if button1.pressed: #if button1 is pressed, rgb turns on
            switch('red')
            switch('red')
            switch('red')
            switch('red')
            button1.pressed = False
        if button2.pressed: #iff button 2 is pressed, rgb turns on
            switch('green')
            switch('blue')
            switch('red')
            switch('green')
            switch('blue')
            switch('red')
            button2.pressed = False
        
except KeyboardInterrupt:
    rgb.turnRGB_off() #turns rgb light ooff
    sleep(1)

finally:
    rpi.GPIO.cleanup() #clean up board
