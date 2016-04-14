from board import Board
import time

class Button:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.pin = pin
        self.__button()
        self.__pressed = False
        
    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value

    def __button(self, resistor = False):
        if not resistor:
            self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN)
        elif resistor:
            self.__board.GPIO.set(self.pin, self.__board.GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        else:
            print('Error in setting up the resistor')
        
    def __my_callback(self, channel):
        self.pressed = True
        
if __name__ == "__main__":
  
    rpi = Board()
    button = Button(rpi, 24)

    while True:
        if button.pressed:
            print('Button Pressed')
            button.pressed = False
        time.sleep(0.2)
    rpi.GPIO.cleanup()
