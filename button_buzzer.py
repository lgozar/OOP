from board import Board
from button_class import Button
from buzzer_class import Buzzer
from time import sleep

rpi = Board()
button1 = Button(rpi, 24)
button2 = Button(rpi, 12)
buzz = Buzzer(rpi, 11)

try:
    
    print('Ready!')
    sleep(0.2)
    print('Press button to buzz')
    
    while True:
        '''press button to buzz'''
        if button1.pressed:
            buzz.beep()
            buzz.stop()
            button1.pressed = False
        if button2.pressed:
            buzz.beep()
            buzz.stop()
            button2.pressed = False
            
except KeyboardInterrupt:
    buzz.stop()
    sleep(0.1)
    
finally:
    buzz.stop()
