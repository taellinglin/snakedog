from .scene import BaseScene
from config import Font


class StartScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Font.default
        self.title = self.font.render("Welcome to the game!", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.game.screen.get_rect().get_center()

    def render(self):
        self.game.screen.blit(self.title, self.title_rect)
