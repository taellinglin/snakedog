# setup stuff here
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from engine import music
import logging
import pygame
from pygame import font
import sys

fmt = "[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s"

logging.basicConfig(
    filename="game.debug.log", level=logging.DEBUG, filemode="w", format=fmt
)
logging.info("loaded logger from config")

root = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
root.addHandler(handler)


def hex_to_rgb(value):
    value = value.lstrip("#")
    lv = len(value)
    rgb = tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))
    # print(str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]))
    return rgb


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()
pygame.font.init()

MAP_COLLISION_LAYER = 1


class Fonts:
    # default = font.Font("resources/fonts/Daemon_Full_Working.otf", 32)
    default = pygame.font.Font("freesansbold.ttf", 32)


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
