from board import Board
import time

class MorseCode:

    def ___init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup()
        self.__main()
        
    def __setup(self):
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.OUT)
        
    def __main(self):
    
        '''dot dot dot'''
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)

        '''dash dash dash'''
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.2)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.2)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.2)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.2)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.2)
    
        '''dot dot dot'''
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)
        time.sleep(0.1)
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)
        time.sleep(0.1)
    
        
        
