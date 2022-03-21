import pygame

from .scene import BaseScene
from config import Font
from components import Grid, Tile


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.grid = Grid(0, 0, 8, 8, 64, 64)

        for i in range(len(self.grid.grid)):
            for j in range(len(self.grid.grid[i])):
                self.grid.set_cell(i, j, Tile("tile"))

    def render(self):
        self.grid.update()