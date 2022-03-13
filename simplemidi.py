from IPython.display import Audio
from pretty_midi import PrettyMIDI

class simplemidi():
    def playmidi(midi_file, sf2_path):
        music = PrettyMIDI(midi_file=midi_file)
        waveform = music.fluidsynth(fs = 192000000, sf2_path=sf2_path)
        Audio(waveform, rate=44100)