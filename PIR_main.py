from board import Board
from PIR_class import PIR
from time import sleep

rpi = Board()
pir = PIR(rpi, 17)

pir.main()
