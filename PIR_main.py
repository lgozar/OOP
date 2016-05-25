from board import Board #import Board class 
from PIR_class import PIR #import PIR class
from time import sleep

rpi = Board() #implement Board class to variable rpi
lcd = LCD(rpi)
pir = PIR(rpi, 17) #implement PIR class to variable pir with pin 17

try:
    print('Starting PIR sensor..')
    sleep(0.2)
    print('Ready!')
    while True:
        pir.main() #runs the main property from the PIR class
        sleep(0.1)
        
except KeyboardInterrupt:
    print('Stop')
    pir.stop() #clean up pins
