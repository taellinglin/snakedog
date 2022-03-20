from pydub import AudioSegment
from pydub.playback import play

audiofile = "synthesizer.wav"
start_ms = 0
end_ms = 16000

sound = AudioSegment.from_file(audiofile, format="wav")
splice = list(sound)[end_ms:start_ms:-1]
play(splice)
