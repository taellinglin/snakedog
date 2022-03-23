import pygame

from engine import music
from .scene import BaseScene
from config import Color, Fonts


class StartScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Fonts.default
        self.title = self.font.render(
            "Welcome to the game! Press W to start",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.game.screen.get_rect().center
        self.soundtrack = music.music

        self.soundtrack.playBgm("resources/audio/music/JazzPad2.ogg", 0.25, True)

    def render(self):
        self.game.screen.blit(self.title, self.title_rect)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.game.scene = self.game.scenes.menu
