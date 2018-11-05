#Uke.py
#Should be a singleton
import os, Song, NewExceptions

class Uke:
    def __init__(self):
        self.allSongs = []
        print("Running Auto-Import.")
        self.autoImport();
        print()
    
    def play(self, songNum):
        self.allSongs[songNum].play()
    
    def printSong(self):
        pass
    
    def getSong(self,songName):
        try:
            for song in self.allSongs:
                if(song.getName()==songName):
                    print("Song already imported.")
                    return 1
            self.allSongs.append(Song.Song(songName))
            return 0
        except:
            return 1
    
    def listSongs(self):
        if(len(self.allSongs)<1):
            print("No songs imported!")
        i = 1
        for song in self.allSongs:
            print(str(i)+". "+song.getName())
            i+=1
    
    def numSongs(self):
        return len(self.allSongs)
    
    def autoImport(self):
        directories = os.listdir('Songs')
        for d in directories:
            if d.find('.txt')!=-1:
                self.getSong(d)