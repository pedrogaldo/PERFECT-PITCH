from midiutil import MIDIFile
from mido import MidiFile, MidiTrack, Message

mid = MidiFile()
track = MidiTrack
mid.tracks.append(track)

Message('note_on', channel=2, note=16, velocity=32, time=0),
Message('note_off', channel=2, note=16, velocity=32, time=0)

##aca asociamos notas con la/s frecuencia 


def crearNota(nota, duration, velocity):
    
    Message('note_on', channel=1, note=nota, velocity=32, time=duration)

