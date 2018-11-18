import time
from cosmicrain import Modulate
import RPi.GPIO as GPIO
from PiPocketGeiger import RadiationWatch

geigerSignalPin=40
geigerNoisePin=38
lightSensorPin
lightCalibration = 10 #find an average calibration
geigerCalibration = 10 #find an average calibration

class geiger:
    def __init__(self):
        self.pingCount = [0]*15
        self.lastPingTime = 0
        self.currentPingTime = 0
        self.g = RadiationWatch(geigerSignalPin, geigerNoisePin, numbering=GPIO.BOARD)
        self.g.register_radiation_callback(onRad)
        self.g.register_noise_callback(onNoise)
        
    def onRad(self):
        print('Ping')
        self.currentPingTime = time.localtime()[5]%15
        if(self.currentPingTime!=self.lastPingTime):
            self.pingCount[self.currentPingTime] = 1
        else:
            self.pingCount[self.currentPingTime] += 1
        tot = sum(self.pingCount)
        if (tot>geigerCalibration):
            Modulate.geigerMod(tot-geigerCalibration)
        return
    
    def onNoise(self):
        print('Noise')
        pass
    
    def getSum(self):
        return sum(self.pingCount)
       
        
class lightSensor:
    def __init__(self):
        self.pingCount = [0]*15
        self.lastPingTime = 0
        self.currentPingTime = 0
        self.l = LightSensor(lightSensorPin)
        self.l.register_light_callback(onLight)
    
    def onLight(self):
        print('Ping')
        self.currentPingTime = time.localtime()[5]%15
        if(self.currentPingTime!=self.lastPingTime):
            self.pingCount[self.currentPingTime] = 1
        else:
            self.pingCount[self.currentPingTime] += 1
        tot = sum(self.pingCount)
        if (tot>geigerCalibration):
            Modulate.lightMod(tot-lightCalibration)
            
        return
    
    def getSum(self):
        return sum(self.pingCount)
    
    

'''
Sensitivity can be low, medium, or high
'''
def calibrate(sensitivity='medium'):
    g1 = geiger()
    l1 = lightSensor()
    time.sleep(15.3)
    gAverage += g1.getSum()
    lAverage += l1.getSum()
    time.sleep(15.3)
    gAverage += g1.getSum()
    lAverage += l1.getSum()
    gAverage = gAverage/2
    lAverage = lAverage/2
    if(sensativity='low'):
        geigerCalibration = gAverage*0.9
        lightCalibration = lAverage*0.9
    elif(sensativity='medium'):
        geigerCalibration = gAverage - 1 
        lightCalibration = lAverage - 1
    else:
        geigerCalibration = gAverage*1.1
        lightCalibration = lAverage*1.1
    
    return
        
        
    
    