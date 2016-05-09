import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)

count = 0

def morsecode():
    
    '''dot dot dot'''
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)

    '''dash dash dash'''
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.2)
    
    '''dot dot dot'''
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.1)
    
os.system('clear')
print('Morse Code')

count = input('How many times would you like the SOS to loop?: ')
while count > 0:
    count -= 1
    morsecode()
