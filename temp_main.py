import os
import time
import RPi.GPIO as GPIO
from board import Board
from button_class import Button
from rgb_class import RGB

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

sensor = '/sys/bus/w1/devices/28-021565382dff/w1_slave'

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
rgb = RGB(board, 16, 20, 21)
button1 = Button(board, 24)
button2 = Button(board, 12)

def set_temp(current):

    temp = int(current)
    
    for value in temp:
        
        if button1.pressed:
            value += 1
            button2.pressed = False
        elif button2.pressed:
            value -= 1
            button1.pressed = False

try:
    
    current_temp = set_temp(22)
    
    while True:
        c = read_temp()
        celsius = str(float(round(c, 2)))
        msg = celsius + ' degress C'
        print(msg)
            
        if c < current_temp:
            rgb.turnRGB_off()
            rgb.turnRed_on()
        elif c >= current_temp:
            rgb.turnRGB_off()
            rgb.turnGreen_on()
        else:
            print('Error')
        time.sleep(1)
        

except KeyboardInterrupt:
    rgb.turnRGB_off()
    time.sleep(1)

finally:
    GPIO.cleanup()
