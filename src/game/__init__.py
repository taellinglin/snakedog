import logging
import pygame

import config
from config import Color
import scenes

from animations import Shake, Bounce


class Game:
    def __init__(self):
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
            level_select = scenes.LevelSelect(self)

        self.scenes = Scenes()

        class Animations(object):
            bounce = Bounce(120, 0, 20)
            shake = Shake(-5, 5)
            pass

        self.animations = Animations()

        # set first scene
        self.scene = self.scenes.level_select

        self.clock = pygame.time.Clock()

    def update_animations(self):
        # Have to manually enumerate animations and add conditions
        self.animations.bounce.update()
        self.animations.shake.update()

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
