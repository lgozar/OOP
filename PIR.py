from board import Board

class PIR:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        
    def setup_pir():
        self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN)
        
