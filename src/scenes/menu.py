from config import Color
from config import Font
from .scene import BaseScene


class Menu(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Font.default
        self.title = self.font.render(
            "You are in menu selection. Press W to start",
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        self.title_rect = self.title[1]
        self.title_rect.center = self.game.screen.get_rect().center

    def render(self):
        self.game.screen.blit(self.title[0], self.title_rect)
