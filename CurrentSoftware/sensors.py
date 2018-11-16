import os
import time
import RPi.GPIO as GPIO
from PiPocketGeiger import RadiationWatch


lightSensorPinNum = 15
geigerCounterSg = 18
geigerCounterNs = 16

class GeigerCounter:
    def __init__(self):
        self.radWatch = RadiationWatch(geigerCounterSg,geigerCounterNs,numbering=GPIO.BOARD).setup()
    def getCMP(self):
        return self.radWatch.status()['cpm']
    def getDuration(self):
        return self.radWatch.status()['Duration']
    def getuSvh(self):
        return self.radWatch.status()['uSvh']
    def getuSvhError(self):
        return self.radWatch.status()['uSvhError']
    
    
class LightSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(lightSensorPinNum, GPIO.IN)
        self.total = 0
        
    def LightVal(self):
        x = GPIO.input(PinVal)
        if(x==0):
            self.total=0
            return self.total
        self.total+=1
        return self.total
    
def main()
    g = GeigerCounter()
    L = LightSensor()
    

def calibrate():
    pass
    
if __name__=='__main__':
    main()
    