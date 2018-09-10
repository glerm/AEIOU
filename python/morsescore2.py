from music21 import *
import morse_talk as morse
import random

tempoBPM = 120 #bpm
assinatura='3/8'

environment.set('musicxmlPath', '/usr/bin/musescore')


#texto = "AEIOU"
texto="manifesto desaceleracionista infinitesimal"


m=morse.encode(texto)

M=m.replace(" ", "§") #inserindo um delimitador para os espaços em branco do texto

s=stream.Stream()
s.insert(0, tempo.MetronomeMark(number=tempoBPM))

s.insert(0, metadata.Metadata())
s.metadata.title = texto
s.metadata.composer = 'Agência de Emprego Intergalático Ontológico Único (A.E.I.O.U.)'

s.append(meter.TimeSignature(assinatura))

LA=['A3', 'A4', 'A6']
MI=['E4', 'E5', 'E6']
DO=['C4', 'C5', 'C6']



#chordDASH=chord.Chord(['A4', 'E4', 'A5'],quarterLength=1)
#noteDASH=note.Note('A4',quarterLength=1)
#noteDOT=note.Note('A5',quarterLength=1/3)
restDOT=note.Rest('A5',quarterLength=1/3)

notelist=[]

for m in M:
	chordDASH=chord.Chord([random.choice(LA), random.choice(MI), random.choice(DO)],quarterLength=1)
	noteDOT=note.Note(random.choice(LA),quarterLength=1/3)
	if (m=="-"):		
		notelist.append(chordDASH)
	if (m=="."):
		notelist.append(noteDOT)
	if (m == '§'):
		notelist.append(restDOT)


for n in notelist:
	s.repeatAppend(n,1)


s.show("musicXML")