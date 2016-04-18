import os
import time
import RPi.GPIO as GPIO
from board import Board

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

sensor = '/sys/bus/w1/devices/28-021565382dff/w1_slave'

pins = [16, 20, 21]

set_temp = 22

def setup_pins():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def set_led(colour):
    
    r = 16
    g = 20
    b = 21
    
    if colour == 'red':
        GPIO.output(r, GPIO.HIGH)
    elif colour == 'green':
        GPIO.output(g, GPIO.HIGH)
    elif colour == 'blue':
        GPIO.output(b, GPIO.HIGH)
    else:
        print('Error')
        
def led_off():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def temp_raw():
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    output = lines[1].find('t=')
    if output != -1:
        string = lines[1].strip()[output+2:]
        c = float(string) / 1000.0
        return c

'''main code'''

board = Board()
setup_pins()

try:
    while True:
        c = read_temp()
        if c < set_temp:
            led_off()
            set_led('red')
            print(c)
        elif c >= set_temp:
            led_off()
            set_led('green')
            print(c)
        else:
            print('Error')
        time.sleep(1)

except KeyboardInterrupt:
    led_off()
    time.sleep(1)

finally:
    GPIO.cleanup()
