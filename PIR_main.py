from board import Board
from PIR_class import PIR
from time import sleep

rpi = Board()
pir = PIR(rpi, 17)

try:
    print('Starting PIR sensor..')
    sleep(0.2)
    print('Ready!')
    while True:
        pir.main()
        sleep(0.1)
        
except KeyboardInterrupt:
    print('Stop')
    pir.stop()
