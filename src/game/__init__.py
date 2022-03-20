import pygame

import config
from engine import imageManager
from util import Singleton
import scenes


class Scenes(object):
    pass


class Game(Singleton):
    def __init__(self):
        self.running = False
        self.screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        )

        self.scenes = Scenes()

        # Add many more screens later
        self.scenes.start_screen = scenes.StartScreen(self)
        self.scenes.menu = scenes.Menu(self)

        # set first scene
        self.scene = self.scenes.start_screen

        self.clock = pygame.time.Clock()

    def main(self):
        """
        Blocking entry point for the entire game
        """
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if self.event(event):
                    continue
                if self.scene.event(event):
                    continue
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            self.scene.render()

            pygame.display.update()

            self.clock.tick(60)

    def event(self, event):
        pass


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for x in range(width)] for y in range(height)]

    def check(self, x, y):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return True
        raise Exception("Invalid cell coordinates")

    def set_cell(self, x, y, cell):
        self.check(x, y)
        self.grid[y][x] = cell

    def get_cell(self, x, y):
        self.check(x, y)
        return self.grid[y][x]


class BaseTile(pygame.sprite.Sprite):
    def __init__(self, image=None):
        if image:
            self.image = image
            self.rect = self.image.get_rect()

    def update(self):
        raise Exception("BaseTile should be implemented by another class")


class TileEntity(BaseTile):
    def __init__(self, type, x, y):
        # Implement loading many other images too
        super().__init__(imageManager.get_resource(type))
        self.x, self.y = (x, y)  # where it is in the game engine

        self.render_vx = 0
        self.render_vy = 0

    def update(self):
        # make sure to move rendering pos to physical pos gradually
        # use vx and vy
        pass


class Tile(BaseTile):
    def __init__(self, type):
        super().__init__(imageManager.get_resource(type))

    def update(self):
        # literally just have to draw
        pass
