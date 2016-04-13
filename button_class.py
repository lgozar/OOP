from board import Board
import time

class Button:
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.pin = pin
        self.button()
        self.__pressed = False
        
    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value
        
    def button(self)
        self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN, pull_up_down = self.__board.GPIO.PUD_UP)
        
if __name__ == "__main__":
  
    rpi = Board()
    button = Button(rpi, 24)
    
    while True: 
        if button.pressed:
            print('button pressed')
            button.pressed = False    
    rpi.GPIO.cleanup()
