import pygame

from .scene import BaseScene
from config import Font
from config import Color


class Menu(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Font.default
        self.title = self.font.render(
            "You are in level selection. Press W to start",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.game.screen.get_rect().center

    def render(self):
        self.game.screen.blit(self.title, self.title_rect)
