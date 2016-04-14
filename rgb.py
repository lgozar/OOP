from board import Board
from time import sleep

class RGB:

    def __init__(self, gpio_object, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        self.__outputs = [self.red, self.green, self.blue]
        self.board = gpio_object
        
        self.setup_led()
        
    def setup_led(self):
        print('Setting up pins')
        for pins in self.__outputs:
            self.board.GPIO.setup(pins, self.board.GPIO.OUT)
        
    def turnRed_on(self):
        self.turnRGB_off()
        self.board.GPIO.output(self.red, self.board.GPIO.HIGH)
    
    def turnBlue_on(self): 
        self.turnRGB_off()
        self.board.GPIO.output(self.blue, self.board.GPIO.HIGH)
        
    def turnGreen_on(self): 
        self.turnRGB_off()
        self.board.GPIO.output(self.green, self.board.GPIO.HIGH)
        
    def turnRGB_off(self):
        for pins in self.__outputs:
            self.board.GPIO.output(pins, self.board.GPIO.LOW)
        
if __name__ == "__main__":

    rpi = Board()
    rgb = RGB(rpi, 16, 20, 21)
    rgb.turnRed_on()
    sleep(0.1)
    rgb.turnGreen_on()
    sleep(0.1)
    rgb.turnBlue_on()
    sleep(0.1)
    rgb.turnRGB_off()
