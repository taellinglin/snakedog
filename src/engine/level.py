import pygame
import pytmx
from engine.layer import Layer
from engine.tile import Tile


class Level(object):
    def __init__(self, fileName, tiles):
        # Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(fileName)
        # Create gruop of tiles for this layer
        self.tiles = tiles
        # Create list of layers for map
        self.layers = []

        # Amount of level shift left/right
        self.levelShift = 0

        # Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(
                Layer(index=layer, mapObject=self.mapObject, tiles=tiles)
            )

    # Move layer left/right
    def shiftLevel(self, shiftX, shiftY):
        self.levelShift += shiftX
        self.levelShift += shiftY

        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
                tile.rect.y += shiftY

    # Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)

    # Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)


# Sprit sheet class to load sprites from player spritesheet
