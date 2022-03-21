import pygame

from .scene import BaseScene
from config import Font


class Menu(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Font.default
        self.title = self.font.render(
            "You are in level selection. Press W to start",
            True,
            (0, 255, 0),
            (255, 0, 0),
        )
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.game.screen.get_rect().center

    def render(self):
        self.game.screen.blit(self.title, self.title_rect)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.game.scene = self.game.scenes.game_scene
