#numpy
import numpy as np #para guardar datos en arrays

#para graficar diferentes cosas dentro del arhivo de audio
import seaborn
import matplotlib.pyplot as plt

#IPython
import IPython.display as ipd

#librosa
import librosa, librosa.display #para cargar y procesar audio 

#MIDIUtil
#from MidiUtil import MIDIFile #generar archivos MIDI
from music21.tempo import MetronomeMark #sacar el tempo de una cancion
from music21.note import Note, Rest 
from music21.stream import Stream
from music21 import metadata 
from music21 import midi #generar notas MIDI
from music21.key import Key #sacar la tonalidad de la cancion







x, sr = librosa.load('/content/pruab.mp3')
ipd.Audio (x, rate=sr)



#forma de onda
plt.figure(figsize=(10,5))
librosa.display.waveplot(x,sr)



#estima adonde hay un onset
onsets = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)


onset_segs = librosa.frames_to_time(onsets) #convierte la estimacion de los onsets a segundos
print(onset_segs)




#grafico de los onsets sobre la forma de onda

plt.figure(figsize=(10, 5))
librosa.display.waveplot(x, sr=sr)
plt.vlines(onset_segs, -0.15, 0.15, color='r', alpha=0.7) 




