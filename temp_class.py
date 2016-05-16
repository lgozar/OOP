import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

sensor = '/sys/bus/w1/devices/28-021565382dff/w1_slave'

class Temperature:

    def __init__(self):
        pass
      
    @property
    def c(self):
        return self.read_temp()
        
    def __temp_raw(self):
        f = open(sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def read_temp(self):
        lines = self.__temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.__temp_raw()
        output = lines[1].find('t=')
        if output != -1:
            string = lines[1][output+2:]
            c = float(string) / 1000.0
            return c
            
if __name__ == '__main__':
    temp_sensor = Temperature()
    print('Temperature = ' + str(int(temp_sensor.c)) + ' C')
