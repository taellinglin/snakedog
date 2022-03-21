import pygame
from engine.tile import Tile


class Layer(object):
    def __init__(self, index, mapObject, tiles):
        # Layer index from tiled map
        self.index = index

        # Reference map object
        self.mapObject = mapObject
        self.tiles = tiles
        # Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(
                        Tile(
                            image=img,
                            x=(x * self.mapObject.tilewidth),
                            y=(y * self.mapObject.tileheight),
                        )
                    )
