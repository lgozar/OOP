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

'''        
    def __my_callback(self, channel):
        self.pressed = True
''''

if __name__ == "__main__":
  
    rpi = Board()
    button = Button(rpi, 24)

    while True:
        if button.pressed:
            print('Button Pressed')
            button.pressed = False
    rpi.GPIO.cleanup()
