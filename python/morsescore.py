from music21 import *
import morse_talk as morse
import random

tempoBPM = 180 #bpm
assinatura='6/8'

environment.set('musicxmlPath', '/usr/bin/musescore')


#texto = "AEIOU"
#texto="manifesto desaceleracionista infinitesimal"
texto="seus ossos somos isso sos"


m=morse.encode(texto)

M=m.replace(" ", "§") #inserindo um delimitador para os espaços em branco do texto
M=M.replace("§§§", "|") #operação para deixar simetria entre palavras
M=M.replace("§", "") #operação para deixar simetria entre palavras


#print (M)

s=stream.Stream()
s.insert(0, tempo.MetronomeMark(number=tempoBPM))

s.insert(0, metadata.Metadata())
s.metadata.title = texto
s.metadata.composer = 'Agência de Emprego Intergalático Ontológico Único (A.E.I.O.U.)'

s.append(meter.TimeSignature(assinatura))


chordDASH=chord.Chord(['A4', 'E4', 'A5'],quarterLength=1)
#noteDASH=note.Note('A5',quarterLength=1)
chordDOT=chord.Chord(['A3', 'C4', 'A4'],quarterLength=1/3)
#noteDOT=note.Note('A5',quarterLength=1/3)
restDOT=note.Rest('A5',quarterLength=1/3)
#restDASH=note.Rest('A5',quarterLength=1)

notelist=[]

for m in M:
	if (m=="-"):		
		notelist.append(chordDASH)
	if (m=="."):
		notelist.append(chordDOT)
	if (m == '|'):
		notelist.append(restDOT)
		notelist.append(restDOT)
		notelist.append(restDOT)

for n in notelist:
	s.repeatAppend(n,1)


#s.show("text")
s.show("musicXML")