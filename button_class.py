from board import Board
from time import sleep

class Button:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__button()
        self.__pressed = False
        
    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value
        

    def __button(self):
        
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN, pull_up_down = self.__board.GPIO.PUD_UP)
            
        self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback = self.__my_callback, bouncetime = 300)

    def __my_callback(self, channel):
        
        self.pressed = True
