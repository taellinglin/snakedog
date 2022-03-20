import pygame
import wave
import pyaudio
from pygame import mixer


wf = wave.open("synthesizer.wav", "rb")

audio_length = wf.getnframes() / wf.getframerate()

# p = pyaudio.PyAudio()

# stream = p.open(
#     format=p.get_format_from_width(wf.getsampwidth()),
#     channels=wf.getnchannels(),
#     rate=wf.getframerate(),
#     output=True,
# )

# full_data = []
# data = wf.readframes(1024)

# while data:
#     full_data.append(data)
#     data = wf.readframes(1024)

# data = full_data[::-1]

# for d in data:
#     stream.write(d)

pygame.init()
mixer.pre_init()
pygame.display.set_caption("Mixer Test")
pygame.display.set_mode((400, 400))

mixer.music.load("synthesizer.wav")
mixer.music.play(0, 10)

last_audio_loc = 0

audio_flow_mode = True  # True -> going forward

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if audio_flow_mode:
                    last_audio_loc += mixer.music.get_pos()
                    print(f"going backwards. playing at {last_audio_loc}")
                    mixer.music.stop()
                    mixer.music.load("reversed-synth.wav")
                    mixer.music.play(0, audio_length - last_audio_loc)
                else:
                    last_audio_loc -= mixer.music.get_pos()
                    print(f"going forward. playing at {last_audio_loc}")
                    mixer.music.stop()
                    mixer.music.load("synthesizer.wav")
                    mixer.music.play(0, last_audio_loc)
                audio_flow_mode = not audio_flow_mode

        pygame.display.update()
        pygame.time.Clock().tick(60)
