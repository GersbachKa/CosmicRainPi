import time
import os
import RPi.GPIO as GPIO

class fineTest:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.pin = 7 #Pin number of data wire
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin,50)
        self.pwm.start(5)
        self.pwm.ChangeDutyCycle(2.5)
        self.location = 0
    
    def goTo(self, degrees):
        factor = 18
        if(type(degrees)!=type(factor)):
            print("Degree out of range, Use between 0 and 180. Use an integer.")
            return
        elif(degrees>180):
            print("Degree out of range, Use between 0 and 180. Use an integer.")
            return
        elif(degrees<0):
            print("Degree out of range, Use between 0 and 180. Use an integer.")
            return
        else:
            self.pwm.ChangeDutyCycle(degrees/factor)
            print("Moved to : "+ degrees +" degrees.")
            return
    
    def clean(self):
        GPIO.cleanup()
        exit()
    