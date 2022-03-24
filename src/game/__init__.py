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

        # screen has to be loaded first because of some of the
        # utilities we are using
        self.screen = config.screen

        # Add many more screens later
        class Scenes(object):
            start_screen = scenes.StartScreen(self)
            menu = scenes.Menu(self)
            game_scene = scenes.GameScene(self)
            level_select = scenes.LevelSelect(self)
            uitest = scenes.UITest(self)

        self.scenes = Scenes()

        class Animations(object):
            bounce = Bounce(120, 0, 20)
            shake = Shake(-5, 5)
            pass

        self.animations = Animations()

        # set first scene
        self.scene = self.scenes.game_scene

        self.level = 1

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
            self.fps = self.clock.get_fps()

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

            self.draw_fps()

            pygame.display.update()

            self.clock.tick(60)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self.scenes.game_scene.level = level
        self._level = level

    def event(self, event):
        pass

    def draw_fps(self):
        fps_text = config.Font.default.render(
            "FPS: " + str(int(self.fps)), True, Color.TEXT_COLOR, (0, 0, 0, 20)
        )

        self.screen.blit(fps_text, (0, 0))
