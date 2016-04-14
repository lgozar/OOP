from board import Board
import time

class Button:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.pin = pin
        self.__button()
        
    def __button(self):
        self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN, pull_up_down = self.__board.GPIO.PUD_UP)
        
if __name__ == "__main__":
  
    rpi = Board()
    button = Button(rpi, 24)
    
    while True:
        if button:
            print('Button Pressed')
            time.sleep(0.2)
    rpi.GPIO.cleanup()
