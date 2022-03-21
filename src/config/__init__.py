# setup stuff here

import enum
import logging
import pygame

logging.basicConfig(filename="game.debug.log", level=logging.DEBUG, filemode="w")
logging.info("loaded logger from config")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()
pygame.font.init()

# TODO
# Fill out these classes


class Font:
    default = pygame.font.Font("freesansbold.ttf", 32)


class Color(enum):
    def hex_to_rgb(value):
        value = value.lstrip("#")
        lv = len(value)
        return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))

    BACKGROUND = hex_to_rgb("#460D3A") + 1.0  # Background Color
    TEXT_COLOR = hex_to_rgb("#000000") + 1.0  # Normal Text Color
    TEXT_INVERSE = hex_to_rgb("#FFFFFF") + 1.0  # Inverted Text Color
    TEXT_RED = hex_to_rgb("FF0000") + 1.0  # Names are red
    TEXT_GREEN = hex_to_rgb("00FF00") + 1.0  # Places are green
    TEXT_BLUE = hex_to_rgb("0000FF") + 1.0  # Things are blue
    BORDER_ONE = hex_to_rgb("0ED1F0") + 1.0  # Border Color One
    BORDER_TWO = hex_to_rgb("F0CD00") + 1.0  # Border Color Two
