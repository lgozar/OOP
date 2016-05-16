import RPi.GPIO
from time import sleep

class Board:

    def __init__(self):
        self.GPIO = RPi.GPIO
        self.__setup()
        
    def __setup(self):
        #setting the mode
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        
    def clean_up(self):
        #turns off the pins
        self.GPIO.cleanup()
