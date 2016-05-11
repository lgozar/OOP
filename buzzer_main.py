from board import Board
from buzzer_class import Buzzer

rpi = Board()
buzz = Buzzer(rpi, 11)

buzz.beep()
buzz.beep()
buzz.stop()
