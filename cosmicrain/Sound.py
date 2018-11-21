#Sound.py
import time 
from cosmicrain import NewExceptions

downFret = 485
upFret = 450
buffer = .2
pcCompat = False

try:
    from cosmicrain import ServoController as sc
    from cosmicrain import Strummer
except:
    from cosmicrain import SoundController as snd
    pcCompat = True


#Available notes: G0,G#0,B0,C0,C1,D1,E1,F1,E2,F2,G2,A3,B3,C3,D3 
class Sound:
    #notesToServos DICTIONARY
    npins = {
        'G0':-1, #Number in string corresponds to the string to play
        'G#0':4,
        'B0':5,
        'C0':6,
        'C1':-1,
        'D1':7,
        'E1':8,
        'F1':9,
        'E2':-1,
        'F2':10,
        'G2':11,
        'A3':-1,
        'B3':12,
        'C3':13,
        'D3':14,
        'REST':-1
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

        sc.move(Sound.npins[self.note],downFret) #Fret down
        time.sleep(buffer) #Wait for fret to go down
        Strummer.strummer(int(self.note[-1])) #Strum
        time.sleep(buffer) #Wait for strum
        sc.move(Sound.npins[self.note],upFret) #Fret up
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
            sc.move(Sound.npins[note],downFret) #Move them all down
        time.sleep(buffer) #Wait for fret
        for note in self.notes: #Move strummers
            Strummer.strummer(int(note[-1])) #Strum
        time.sleep(buffer) #wait for strum
        for note in self.notes: #Move down frets
            sc.move(Sound.npins[note],upFret) #Move them all down
        return

    def __str__(self):
        return self.notes
