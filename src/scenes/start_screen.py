import keyboard
from .scene import BaseScene


class StartScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.soundtrack = None
        self.title_rect = None
        self.title = None

    def render(self):
        self.game.screen.blit(self.title[0], self.title_rect)

    def event(self, event):
        if keyboard.is_select(event):
            self.soundtrack.stop()
            self.game.scene = self.game.scenes.level_select
