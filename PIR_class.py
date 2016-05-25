from board import Board
from time import sleep

class PIR:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup_pir()
        
    def __setup_pir(self):
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN)
        
    def main(self):
        self.__board.GPIO.input(self.__pin):
            
    def stop(self):
        self.__board.GPIO.cleanup()
        
