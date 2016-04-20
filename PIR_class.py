
class PIR:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup_pir()
        
    def __setup_pir(self):
        self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN)
        
