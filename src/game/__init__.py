import pygame

import config
from config import Color
from engine import imageManager
from engine import music
from util import Singleton
import scenes
from animations import Bounce


class Game(Singleton):
    def __init__(self):
        super().__init__()

        # Inject self
        pygame.game = self

        self.running = False
        self.screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        )

        # Add many more screens later
        class Scenes(object):
            start_screen = scenes.StartScreen(self)
            menu = scenes.Menu(self)
            game_scene = scenes.GameScene(self)

        self.scenes = Scenes()

        class Animations(object):
            bounce = Bounce(120, 0, 20)

        self.animations = Animations()

        # set first scene
        self.scene = self.scenes.start_screen

        self.clock = pygame.time.Clock()

    def update_animations(self):
        # Have to manually enumerate animations and add conditions
        self.animations.bounce.update()

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

            self.screen.fill(Color.BACKGROUND)

            self.update_animations()

            self.scene.render()

            pygame.display.update()

            self.clock.tick(60)

    def event(self, event):
        pass
