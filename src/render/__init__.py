# Game renderer

import logging
import glob
import re
import os

import pygame

import util
from levels import levels
from engine import World

level_files = {}

__file_regex = re.compile(r"^(\d+).\w+$")

for filepath in glob.glob("resources/mapdata/levels/*.tmx"):
    if m := re.match(__file_regex, os.path.basename(filepath)):
        num = int(m.group(1))
        level_files[num] = filepath
        logging.info(f"Successfully recognized level file {filepath}")
        continue
    logging.error(f"{filepath} is not valid. Ignoring...")


class WorldRender:
    """
    Create a new instance to render another level
    """

    def __init__(self, game, level: int):
        self.level = level
        self.game = game
        self.world = World(
            level_files[level],
            (1000, 1000),
            entity_loader_func=levels[level],
            total_moves=30,
        )

    def render_to(self, screen):
        self.world.render(screen)

    def event(self, event):
        self.world.event(event)
