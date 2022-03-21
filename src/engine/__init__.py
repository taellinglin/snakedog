from .managers import AudioManager, ImageManager

audioManager = AudioManager("resources/audio")
imageManager = ImageManager("resources/images")

imageManager.add_resource("tile", "sprites/test-tile.png")
audioManager.add_resource("Jazzpad", "audio/music/Jazzpad.wav")
audioManager.add_resource("Jazzpad2", "audio/music/Jazzpad2.wav")

