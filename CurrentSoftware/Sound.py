#Sound.py
import time, Strummer, NewExceptions
import ServoController as sc

#Available notes: G0,C1,D1,F1,E2,Gb2,G2,A2,B2,A3,B3,C3,D3,E3 
class Sound:
    #notesToServos DICTIONARY
    npins = {
        'G0':-1, #Number in string corresponds to the string to play
        'C1':4,
        'D1':5,
        'F1':6,
        'E2':-1,
        'GB2':7,
        'G2':8,
        'A2':9,
        'B2':10,
        'A3':-1,
        'B3':11,
        'C3':12,
        'D3':13,
        'E3':14,
        'REST':-1,
    }
    def __init__(self):
        pass
    def play(self):
        pass
    def notepins(inp):
        print(Before)
        print(npins)
        print(inp)
        return Sound.npins[inp]
        
            
class Note(Sound):
    npins = {
        'G0':-1, #Number in string corresponds to the string to play
        'C1':4,
        'D1':5,
        'F1':6,
        'E2':-1,
        'GB2':7,
        'G2':8,
        'A2':9,
        'B2':10,
        'A3':-1,
        'B3':11,
        'C3':12,
        'D3':13,
        'E3':14,
        'REST':-1,
    }
    def __init__(self, innote):
        try:
            print("Note: "+innote.upper())
            notepins(innote.upper())
            print("After")
        except:
            raise NewExceptions.wrongFormatException("Note is not playable")
        self.note = innote.upper()
    
    def play(self): #TOTAL DELAY = 2ms
        if(self.note=='REST'):
            #Don't play, still delay
            return
        if(notepins(self.note)==-1):
            #Delay for fake fret
            time.sleep(.1)
            Strummer.strummer(self.note[-1])
            return
        
        sc.move(notepins(self.note),405) #Fret down
        time.sleep(.1) #Wait for fret to go down
        Strummer.strummer(self.note[-1]) #Strum
        time.sleep(.1) #Wait for strum
        sc.move(notepins(self.note),205) #Fret down
        return
    def notepins(inp):
        print(Before)
        print(npins)
        print(inp)
        return Note.npins[inp]
        
        
        
class Chord(Sound):
    npins = {
        'G0':-1, #Number in string corresponds to the string to play
        'C1':4,
        'D1':5,
        'F1':6,
        'E2':-1,
        'GB2':7,
        'G2':8,
        'A2':9,
        'B2':10,
        'A3':-1,
        'B3':11,
        'C3':12,
        'D3':13,
        'E3':14,
        'REST':-1,
    }
    
    def __init__(self,innotes):
        self.notes=[]
        for n in innotes:
            try:
                notepins(n.upper())
                for a in self.notes:
                    if(n[-1]==a[-1]):
                        raise NewExceptions.wrongFormatException("Two notes on one string")
            except:
                raise NewExceptions.wrongFormatException("Note is not playable")
            self.notes.append(n.upper())
    
    def play(self): #TOTAL DELAY = 2ms
        for note in self.notes: #Move down frets
            sc.move(notepins(note),405) #Move them all down
        time.sleep(.1) #Wait for fret
        for note in self.notes: #Move strummers
            Strummer.strummer(note[-1]) #Strum
        time.sleep(.1) #wait for strum
        for note in self.notes: #Move down frets
            sc.move(notepins(note),205) #Move them all down
        return
    def notepins(inp):
        print(Before)
        print(npins)
        print(inp)
        return Sound.npins[inp]
        