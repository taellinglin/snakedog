from .managers import AudioManager, ImageManager

audioManager = AudioManager("resources/audio")
imageManager = ImageManager("resources/images")

imageManager.add_resource("tile", "sprites/test-tile.png")
