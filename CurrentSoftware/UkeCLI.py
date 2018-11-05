#UkeCLI.py
import os, Ukulele

def main():
    print("Cosmic Rain Ukelele V0.1")
    u = Ukulele.Uke()
    functionSelector(u)
    
def functionSelector(u):
    while(True):
        print("\nAvailable Functions: \n1. Import Song, 2. List Songs, 3.Play Song")
        try:
            i = int(input("Which Function, 0 to exit: "))
        except ValueError:
            i=-1
        if(i<0 or i>3):
            #clear the screen somehow?
            print("Invalid function")
        elif(i==0):
            print("Exiting...")
            break
        else:
            doFunction(u,i)

def doFunction(u,i):
    if(i==1):
        while(True):
            #Print the directory of Songs
            print("Which song to Import?")
            i = 1
            theDir = os.listdir('Songs')
            for file in theDir:
                if(file.find('.txt')==-1):
                    theDir.remove(file)
            
            for file in theDir:
                print(str(i)+". "+file.replace('.txt',''))
                    
            s = input("Song number, type 0 to escape: ")
            if(s=='0'):
                break
            try:
                s=int(s)-1
                temp = u.getSong(theDir[s])
                if(temp==1):
                    print("Import failed.")
                    break
                print("Import Success!")
                break
            except Exception as e:
                print(e)
    if(i==2):
        u.listSongs()
    if(i==3):
        while(True):
            u.listSongs()
            if(u.numSongs()<1):
                break
            s = input("Type the number, type 0 to escape: ")
            if(s=='0'):
                break
            try:
                s = int(s)-1
                u.play(s)
                print("Song Finished.")
                break
            except ValueError as e:
                #print(s)
                #print(e)
                print(S+": Not a valid number")
    
    return

if(__name__=="__main__"):
    main()
