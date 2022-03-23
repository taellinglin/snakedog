import pygame

from .scene import BaseScene
from config import Font


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
