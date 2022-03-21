import pygame

from .scene import BaseScene
from config import Fonts
from config import Color


class Menu(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Fonts.default
        self.title = self.font.render(
            "You are in level selection. Press W to go back",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.game.screen.get_rect().center

    def render(self):
        self.game.screen.blit(self.title, self.title_rect)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.game.scene = self.game.scenes.start_screen
