from datetime import datetime

#Creating variables
now = datetime.now()
date_str = now.strftime("%Y%m%d") 
time_str = now.strftime("%H%M%S") 
counting = 0
pedestrian = "0"
person = 0

#Start by importing all necessary libraries and packages 
import RPi.GPIO as GPIO
import time
from time import sleep
from threading import Thread
from gpiozero import LEDCharDisplay

                        
#number below is a,b,c,d,e,f,g in order. check 7 segment schematic
display = LEDCharDisplay (26, 19, 13, 6, 5, 21, 20, active_high = True) #display tens
display2 = LEDCharDisplay (2, 3, 24, 17, 14, 15, 18, active_high = True) #display ones


#Set the GPIO to BCM Mode
GPIO.setmode(GPIO.BCM)

#Set Pin 4 to be our Sniffer Pin, We want this to be an Input so we set it as such
GPIO.setup(4,GPIO.IN) #pin 4
GPIO.setup(10,GPIO.OUT) #gpio 10
GPIO.setup(27,GPIO.OUT) #gpio 27
GPIO.setup(22,GPIO.OUT) #gpio 22
GPIO.setup(23,GPIO.OUT) #gpio 23
GPIO.setup(24,GPIO.OUT) #gpio 24
GPIO.setup(25,GPIO.OUT) #gpio 25


def vehicleReset():
    outGreen = GPIO.output(10, GPIO.LOW)
    outYellow = GPIO.output(27, GPIO.LOW)
    outRed = GPIO.output(22, GPIO.LOW)

def pedReset():
    outGreen2 = GPIO.output(23, GPIO.LOW)
    outRed2 = GPIO.output(25, GPIO.LOW)
    
    
#Default vehicle traffic red sign
vehicleReset()
pedReset()
time.sleep(1)
outGreen = GPIO.output(10, GPIO.HIGH)

prev_input = 0 #This variable will be used to determine if pressure is being applied or not




while True:
    #Check Pedestrian green light state (on/off)
    pedState = GPIO.input(23)
    #if on, decrease duration
    if pedState:

        def countdown():
            global countInt
            global countGreen
            global doneC
            
            doneC = False

            countGreen = 22 #default timer
            countInt = 7 #internal timer, stops pedestrian green light when no pedestrians stepped on force sensor for a determined period of time


            #if force sensor stepped, refresh internal timer
            while ((countGreen != 0) and (countInt != 0) ):
                countGreen -= 1
                countInt -= 1
                sleep(1)
                print("Default time:")
                print(countGreen)
                print("Internal time:")
                print(countInt)


            
                if countGreen >= 10:
                
                    display.value = str(countGreen)[0]
                    display2.value = str(countGreen)[1]
                    
                elif countGreen < 10:
                    display.off()
                    print(str(countGreen)[0])
                    
                    display2.value = str(countGreen)[0]
                    

            display.off()
            display2.off()
        
            print("Out ")
            doneC = True
            return

        countdown_thread = Thread(target = countdown)
        countdown_thread.start()

        while doneC == False:
            input = GPIO.input(4)
            if (input):
                global countInt
                countInt = 7
        

    #Give green sign to vehicle traffic light if default duration or internal timer goes 0
        #Pedestian red and vehicle yellow
        vehicleReset()
        pedReset()
        outRed2 = GPIO.output(25, GPIO.HIGH)
        outYellow = GPIO.output(27, GPIO.HIGH)
        time.sleep(5)
        
        #Vehicle green
        vehicleReset()
        pedReset()
        outGreen = GPIO.output(10, GPIO.HIGH)

    #take a reading from the pressure pad (based on the voltage able to get to pin 4)
    outGreen = GPIO.output(10, GPIO.HIGH)
    input = GPIO.input(4)
    print(input)

    #if the last reading was low and this one high the pressure pad is being pressed!
    if ((not prev_input) and input):

    #Print that fact to the shell
        #print("Under Pressure")
        
        #Pedestrian Red light
        outRed2 = GPIO.output(25, GPIO.HIGH)
        
        #Vehicle traffic go yellow at the same time
        vehicleReset()
        outYellow = GPIO.output(27, GPIO.HIGH)
        time.sleep(5)
        
        #Vehicle traffic red and pedestrian green (Pedestrian walks)
        vehicleReset()
        pedReset()
        outRed = GPIO.output(22, GPIO.HIGH)
        outGreen2 = GPIO.output(23, GPIO.HIGH)
      

    #update previous input so we can avoid spamming the Shell with messages, 
    #this section of the script is also a perfect place to add threshold values to active other devices 
    prev_input = input

    #Have a slight pause here, also to avoid spamming the shell with data
    time.sleep(0.1)
