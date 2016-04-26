import os
import time
import RPi.GPIO as GPIO
from board import Board
from button_class import Button
from rgb_class import RGB

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

sensor = '/sys/bus/w1/devices/28-021565382dff/w1_slave'

set_temp = 22

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

try:
    while True:
        c = read_temp()
        celsius = str(float(round(c, 2)))
        msg = celsius + ' degress C'
        print(msg)
        
        temp = int(set_temp)
        
        if button1.pressed:
            button2.pressed = False
            temp += 1
        elif button2.pressed:
            button1.pressed = False
            temp - 1
            return temp
                
        if c < temp:
            rgb.turnRGB_off()
            rgb.turnRed_on()
        elif c >= temp:
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
