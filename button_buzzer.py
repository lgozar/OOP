from board import Board
from button_class import Button
from buzzer_class import Buzzer
from time import sleep

rpi = Board()
button = Button(rpi, 24)
buzz = Buzzer(rpi, 11)

try:
    print('Setting up pins..')
    sleep(0.1)
    print('Ready!')
    while True:
        if button.pressed:
            buzz.beep()
            buzz.stop()
            button.pressed = False
            
except KeyboardInterrupt:
    buzz.stop()
    sleep(0.1)
    
finally:
    buzz.stop()
