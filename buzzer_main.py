from board import Board
from buzzer_class import Buzzer

rpi = Board()
buzz = Buzzer(rpi, 11)

count = input('How many times would you want it to loop?: ')

while count > 0:
    count -= 1
    buzz.beep()
    buzz.stop()
