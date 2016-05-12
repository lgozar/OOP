from button_class import Board
from buzzer_class import Buzzer
from time import sleep

rpi = Board()
button = BUtton(rpi, 24)
buzz = Buzzer(rpi, 11)

try:
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
