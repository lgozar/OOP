from board import Board #import board class
from button_class import Button #import button class
from buzzer_class import Buzzer #import buzzer class
from time import sleep # import sleep

rpi = Board() #implement the board class to variable rpi
button1 = Button(rpi, 24) #implement button class to variable button1 with pin 24
button2 = Button(rpi, 12) #implement another button class to variable button2 with pin 12
buzz = Buzzer(rpi, 11) #implement buzzer class to variable buzz with pin 11

try:
    
    print('Ready!')
    sleep(0.2)
    print('Press button to buzz')
    
    while True:
        '''press button to buzz'''
        if button1.pressed: #if button1 is pressed the buzzer buzz
            buzz.beep()
            button1.pressed = False #set button1 to False after press
        if button2.pressed: #if button2 is pressed the buzzer buzz aswell
            buzz.double_beep()
            button2.pressed = False #set button2 to False after press
            
except KeyboardInterrupt:
    buzz.stop() #stops the buzzer
    sleep(0.1)
    
finally:
    buzz.stop() #stops the buzzer
