from board import Board
from PIR_class import PIR
from time import sleep

rpi = Board()
pir = PIR(rpi, 17)

try:
    print('PIR Starting')
    sleep(0.2)
    print('Ready!')
    while True:
        if rpi.GPIO.input(17)
             print('Motion Detected')
        sleep(0.1)
        
except KeyboardInterrupt:
    print('Quit')
    rpi.GPIO.cleanup()
