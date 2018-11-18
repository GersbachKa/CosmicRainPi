'''
Servo limits 205-600
'''

import smbus, time

class _motorHatController:

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.deviceAddr = 0x40
        self.starAddr = []
        self.endAddr = []
        i=6
        while(i<=66):
            self.starAddr.append(i)
            i+=4
        
        i=8
        while(i<=68):
            self.endAddr.append(i)
            i+=4
        
        self.setup()
    
    def close(self):
        self.bus.close()

    def setup(self):
        self.bus.write_byte_data(self.deviceAddr,0,0x20)
        time.sleep(.1)
        self.bus.write_byte_data(self.deviceAddr, 0, 0x10)
        time.sleep(.1)
        self.bus.write_byte_data(self.deviceAddr, 0xFE, 0x79)
        self.bus.write_byte_data(self.deviceAddr,0,0x20)
        
        for a in self.starAddr:
            self.bus.write_word_data(self.deviceAddr,a, 0)
        
        print("Object created")
        
    def mvSr(self,num,inp):
        self.bus.write_word_data(self.deviceAddr,self.endAddr[num],inp)
    


_s = _motorHatController()
def move(num,inp):
    _s.mvSr(num,inp)

def stop():
    _s.close()
