#Strummer.py
import ServoController as sc
strings = [0, 0, 0, 0]
strumPorts = [0,1,2,3]

def strummer(stringNum):
    if(strings[stringNum]==0):
        #move Strummer direction 1
        sc.move(strumPorts[stringNum],405) #Change this to modify the length of rotation
        strings[stringNum]=1
        pass
    else:
        #move Strummer direction 0
        sc.move(strumPorts[stringNum],205) #Change this to modify the length of rotation
        strings[stringNum]=0
        pass
