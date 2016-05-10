from board import Board
from buzzer_class import Buzzer

rpi = Board()
buzz = Buzzer(rpi, 26)

buzz.beep()
buzz.stop()
