
from pygame import mixer
from pygame import USEREVENT
class bgm():
    def __init__():
        mixer.init()

    def playBgm(song=None, volume=1):
        mixer.init()
        mixer.music.load(song)
        pattern = 0
        loop_event = USEREVENT + 1
        mixer.music.set_endevent(loop_event)
        mixer.music.play(start=pattern)
        mixer.music.set_volume(volume)
            
    def update():
        for event in pygame.event.get():
                if event.type == loop_event:
                    pygame.mixer.music.play(start=pattern)

    def set_font(font = None):
        if font != None:
            pass