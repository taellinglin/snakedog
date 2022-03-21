# setup stuff here

from engine import music
import enum
import logging
import pygame
from pygame import font

logging.basicConfig(filename="game.debug.log", level=logging.DEBUG, filemode="w")
logging.info("loaded logger from config")


def hex_to_rgb(value):
    value = value.lstrip("#")
    lv = len(value)
    rgb = tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return rgb


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()
pygame.font.init()


class Fonts:
    default = font.Font("freesansbold.ttf", 32)
    # default = font.Font("resources/fonts/Daemon_Full_Working.otf", 32)


class Color:

    BACKGROUND = hex_to_rgb("#460D3A")  # Background Color
    TEXT_BACKGROUND = hex_to_rgb("#460D3A")  # Text Background
    TEXT_COLOR = hex_to_rgb("#FFFFFF")  # Normal Text Color
    TEXT_INVERSE = hex_to_rgb("#00000")  # Inverted Text Color
    TEXT_RED = hex_to_rgb("#FF0000")  # Names are red
    TEXT_GREEN = hex_to_rgb("#00FF00")  # Places are green
    TEXT_BLUE = hex_to_rgb("#0000FF")  # Things are blue
    BORDER_ONE = hex_to_rgb("#0ED1F0")  # Border Color One
    BORDER_TWO = hex_to_rgb("#F0CD00")  # Border Color Two
