import time
from PiPocketGeiger import RadiationWatch

radwat = RadiationWatch(24,23)
radwat.setup()
print("Status: " + radwat.status())

def onRadiation():
    print("Ray appeared!")
    
def onNoise():
    print("Vibration!")
    
radwat.register_radiation_callback(onRadiation)
radwat.register_noise_callback(onNoise)

while 1:
    time.sleep(1)
    