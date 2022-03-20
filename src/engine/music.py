import pygame
from pygame import mixer
from pygame import USEREVENT


class music:
    def __init__():
        mixer.init()

    def playBgm(song=None, volume=1, loop = True):
        mixer.init()
        mixer.music.load(song)
        pattern = 0
        loop_event = USEREVENT + 1
        mixer.music.set_endevent(loop_event)
        mixer.music.play(start=pattern)
        mixer.music.set_volume(volume)
        for event in pygame.event.get():
            if event.type == loop_event:
                if loop:
                    pygame.mixer.music.play(start=pattern)
                else:
                    pygame.mixer.music.stop()
    def update():
        pass
