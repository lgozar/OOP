from board import Board
from time import sleep

class LED:

    def __init__(self, gpio, pin):
        self.board = gpio
        self.pin = pin
        
    def setup_led(self):
        self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
        
    def turnLED_on(self):
        self.board.GPIO.output(self.pin, self.board.GPIO.HIGH)
        
    def turnLED_off(self):
        self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
        
if __name__ == "__main__"

    rpi = Board()
    led = LED(rpi, pin)
    led.turnLED_on()
    sleep(0.1)
    led.turnLED_off()
