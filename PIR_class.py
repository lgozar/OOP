
class PIR:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup_pir()
        self.__pir_pin = self.__pin
        
    @property
    def pir_pin(self):
        return self.__pir_pin
        
    @pir_pin.setter    
    def pir_pin(self, value):
        self.__pir_pin = value
        
    def __setup_pir(self):
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN)
        
