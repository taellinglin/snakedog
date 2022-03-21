import pygame

import config
from loaders import imageManager
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
        self.scenes.game_scene = scenes.GameScene(self)

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
