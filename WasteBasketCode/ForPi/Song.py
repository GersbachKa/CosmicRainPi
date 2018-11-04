'''
Assumptions:-The name of the song is the same as that of the file.
              Without this, multiple imports of the same song
            -Does not check for accuracy within time signature (Maybe in a future version)
'''
import os, NewExceptions, time

class Song:
    def __init__(self,songName):
        self.noteList = []
        try:
            file = open('Songs/'+songName,"r")
            print("File found!")
            firstline = file.readline().replace('\n','') #Remove the carriage returns
            self.name = firstline.split('\"')[1] #Takes the name given within the quotes
            self.tempo = int(firstline.split(',')[1][7:]) #Takes the number after the "tempo="
            timSigStr = firstline.split(',')[2][6:] #Takes the string after the tempo, EX: "4/4"
            self.timSigUp = int(timSigStr[0:timSigStr.find('/')]) #Takes the value before the / stores as an int
            self.timSigDown = int(timSigStr[timSigStr.find('/')+1:]) #Same as above, but after the /
            
            #Done with the basics, now for the notes
            songStr = file.read().replace('\n','').replace(' ','') #Read the rest of the file, take out all carriage returns and spaces
            measureList = songStr.split('(') #Splits the string by measure
            measureList.remove(measureList[0]) #Removes the empty string at index 0
            for measure in measureList: #For every measure...
                measure = measure.replace(')','').replace(']','') #Removes the ending syntax as they are repetative
                beatList = measure.split('[') #Split based on each beat of a measure
                beatList.remove(beatList[0]) #remove the empty string
                for beat in beatList:
                    if(beat.find(',')==-1): #This means it's only one note
                        if(beat==""):
                            self.noteList.append(Note("REST"))
                        else:
                            self.noteList.append(Note(beat))
                    else: #Chord
                        beat = beat.split(',') 
                        for a in beat: #checks for collisions, multiple notes on one string
                            for b in beat:
                                if a==b:
                                    pass
                                elif a[-1] == b[-1]:
                                    raise NewExceptions.wrongFormatException("Multiple notes on one string")
                        self.noteList.append(Chord(beat))
                    
        except Exception as e:
            print(e) #Tell the user what errors you're getting
            del self
            raise e #Tell the function that an error occured
    
    def getName(self):
        return self.name
    
    def play(self):
        #Incorporate tempo
        for n in noteList:
            n.play()
            time.sleep(1) #Change this value for tempo
        