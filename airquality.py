import csv
from music import *
from midi import *

m = MidiOut("Apple Inc. Bus 1")

duration = 16                                 # duration for each note - 4 measures
tempo = 999



with open('SouthSup.csv', 'rb') as f:
    reader = csv.reader(f)
    superior = list(reader)
    
with open('heights.csv', 'rb') as f:
    reader = csv.reader(f)
    heights = list(reader)
    
with open('EastEnd.csv', 'rb') as f:
    reader = csv.reader(f)
    east = list(reader)
    
with open('Enger.csv', 'rb') as f:
    reader = csv.reader(f)
    enger = list(reader)

superior = [val for sublist in superior for val in sublist]
heights = [val for sublist in heights for val in sublist]
east = [val for sublist in east for val in sublist]
enger = [val for sublist in enger for val in sublist]

phrase = Phrase()
phrase.setTempo(tempo)

length = 602
i = 0
while i < length:
   
   h = float(heights[i])
   ea = float(east[i])
   en = float(enger[i])
   s = float(superior[i])

   pitch_h = mapScale(h, 0, 48, D2, D6, MAJOR_SCALE)   
   pitch_ea = mapScale(ea, 0, 48, D2, D6, MAJOR_SCALE)
   pitch_en = mapScale(en, 0, 48, D2, D6, MAJOR_SCALE)
   pitch_s = mapScale(s, 0, 48, D2, D6, MAJOR_SCALE)
   phrase.addChord([pitch_h, pitch_ea, pitch_en, pitch_s], duration)
   i+=1

m.play(phrase)
print(phrase)