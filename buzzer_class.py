from board import Board
import time

class Buzzer:

    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup()
        
    def __setup(self):
        print('Setting up buzzer..')
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.OUT)
        
    def beep(self):
        '''beep'''
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.1)
        
    def stop(self):
        self.__board.GPIO.cleanup()
        
        
