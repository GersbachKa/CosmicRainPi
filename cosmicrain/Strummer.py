#Strummer.py
from cosmicrain import ServoController as sc
strings = [0, 0, 0, 0]
strumPorts = [0,1,2,3]
strummerLeft = 450
strummerRight = 500

def strummer(stringNum):
    if(strings[stringNum]==0):
        #move Strummer direction 1
        sc.move(strumPorts[stringNum],500) #Change this to modify the length of rotation
        strings[stringNum]=1
        pass
    else:
        #move Strummer direction 0
        sc.move(strumPorts[stringNum],450) #Change this to modify the length of rotation
        strings[stringNum]=0
        pass

def reset():
    strings = [0,0,0,0]