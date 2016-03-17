import RPi.GPIO
from time import sleep

class Board:

    def __init__(self):
        self.GPIO = RPi.GPIO
        self.setup()
        
    def setup():
        #setting the mode
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
