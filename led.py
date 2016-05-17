import RPi.GPIO as GPIO
import time as sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)