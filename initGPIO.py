import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # G
GPIO.setup(21, GPIO.OUT) # R
GPIO.cleanup()