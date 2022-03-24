import logging

import pygame
import random

import music

from .scene import BaseScene
from config import Color, Font

from ui import Button
import keyboard


class UITest(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.button = Button(800, 100, "CONTINUE")
        self.button.x = 0
        self.button.y = 300

    def render(self):
        self.button.update()
        self.game.screen.blit(self.button, (self.button.x, self.button.y))

    def event(self, event):
        if keyboard.is_select(event):
            self.button.press()
            self.button.selected = not self.button.selected
            self.button.text = random.choice(["hi", "test"])
