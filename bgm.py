from pygame import mixer


class bgm:
    def __init__():
        mixer.init()

    def playBgm(song=None, volume=1):
        mixer.init()
        mixer.music.load("bgm/" + song)
        mixer.music.set_volume(volume)
        mixer.music.play()
