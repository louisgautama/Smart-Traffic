#Start by importing all necessary libraries and packages 
import RPi.GPIO as GPIO
import time
from datetime import datetime
now = datetime.now()
date_str = now.strftime("%H%M%S")
print (date_str)
#Set the GPIO to BCM Mode
GPIO.setmode(GPIO.BCM)

#Set Pin 4 to be our Sniffer Pin, We want this to be an Input so we set it as such
GPIO.setup(4,GPIO.IN)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

def vehicleReset():
    outGreen = GPIO.output(10, GPIO.LOW)
    outYellow = GPIO.output(27, GPIO.LOW)
    outRed = GPIO.output(22, GPIO.LOW)

def pedReset():
    outGreen2 = GPIO.output(23, GPIO.LOW)
    outRed2 = GPIO.output(25, GPIO.LOW)
    outYellow2 = GPIO.output(24, GPIO.LOW)

vehicleReset()
pedReset()