#Uke.py
#Should be a singleton
import os, Song

class Uke:
    def __init__(self):
        self.allSongs = []
        print("Running Auto-Import.")
        self.autoImport();
        print()

    def play(self, songNum):
        try:
            self.allSongs[songNum-1].play()
            return 0
        except:
            return 1

    def printSong(self):
        pass

    def getSong(self,songName):
        try:
            for song in self.allSongs:
                if(song.getName()==songName):
                    print("Song already imported.")
                    return 1
            self.allSongs.append(Song(songName))
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
        theDir = os.listdir('Songs')
        for file in theDir:
            if(file.find('.txt')!=-1):
                self.getSong(file)
