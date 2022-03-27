# Game renderer

import glob
import logging
import os
import re

from engine import World
from levels import levels

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

        self.world = None

        if level not in level_files:
            logging.error(f"Level {level} is not valid")
            self.level = 0
            self.game.scene = self.game.scenes.level_select
            return

        self.world = World(
            level_files[level],
            (1000, 1000),
            entity_loader_func=levels[level],
            tile_scale=3,
        )

    def render_to(self, screen):
        if not self.world:
            return
        self.world.render(screen)

    def event(self, event):
        if not self.world:
            return
        self.world.event(event)
