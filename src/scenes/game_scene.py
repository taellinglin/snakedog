import pygame

from render import WorldRender
from .scene import BaseScene
from config import Font


class GameScene(BaseScene):
    """
    Change level to load a new world render
    """

    def __init__(self, game):
        super().__init__(game)
        self.world_render = None

    # This property is always in sync with game.level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        # world_render setting logic
        self._level = level
        if not level:
            self.world_render = None
        else:
            self.world_render = WorldRender(self.game, level)

    def render(self):
        if not self.world_render:
            # TODO redirect to level selection screen
            raise Exception("No world render to render")
        self.world_render.render_to(self.game.screen)

    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                self.world_render.world.reset()
        self.world_render.event(e)
