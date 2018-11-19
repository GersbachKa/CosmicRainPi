#Sound.py
import time 
from cosmicrain import NewExceptions

buffer = .2
pcCompat = False

try:
    from cosmicrain import ServoController as sc
    from cosmicrain import Strummer
except:
    from cosmicrain import SoundController as snd
    pcCompat = True


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
    def __str__(self):
        pass

class Note(Sound):
    def __init__(self, innote):
        try:
            Sound.npins[innote.upper()]
        except:
            raise NewExceptions.wrongFormatException(innote+": Note is not playable")
        self.note = innote.upper()

    def play(self):
        if pcCompat:
            time.sleep(buffer)
            snd.play1(self.note)
            time.sleep(buffer)
            return
        if(self.note=='REST'):
            #Don't play, still delay
            time.sleep(2*buffer)
            return
        if(Sound.npins[self.note]==-1):
            #Delay for fake fret
            time.sleep(buffer)
            Strummer.strummer(int(self.note[-1]))
            time.sleep(buffer)
            return

        sc.move(Sound.npins[self.note],400) #Fret down
        time.sleep(buffer) #Wait for fret to go down
        Strummer.strummer(int(self.note[-1])) #Strum
        time.sleep(buffer) #Wait for strum
        sc.move(Sound.npins[self.note],200) #Fret up
        return

    def __str__(self):
        return self.note

class Chord(Sound):
    def __init__(self,innotes):
        self.notes=[]
        for n in innotes:
            try:
                Sound.npins[n.upper()]
                for a in self.notes:
                    if(n[-1]==a[-1]):
                        raise NewExceptions.wrongFormatException("Two notes on one string")
            except:
                raise NewExceptions.wrongFormatException(n+"Note is not playable")
            self.notes.append(n.upper())
    
    def play(self):
        if pcCompat:
            time.sleep(buffer)
            snd.playN(self.notes)
            time.sleep(buffer)
            return
        for note in self.notes: #Move down frets
            sc.move(Sound.npins[note],400) #Move them all down
        time.sleep(buffer) #Wait for fret
        for note in self.notes: #Move strummers
            Strummer.strummer(int(note[-1])) #Strum
        time.sleep(buffer) #wait for strum
        for note in self.notes: #Move down frets
            sc.move(Sound.npins[note],200) #Move them all down
        return

    def __str__(self):
        return self.notes
