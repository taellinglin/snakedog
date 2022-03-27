# setup stuff here
import os
from random import randrange

# This line has to come before import pygame
# or else pygame will say "Hello from pygame"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
from pygame import freetype

from . import set_logger

pygame.mixer.init()
pygame.freetype.init()
pygame.init()


def hex_to_rgb(value):
    value = value.lstrip("#")

    lv = len(value)
    rgb = tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))

    return rgb


SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

CHEATS = False

SAVE_FILE = "game_save_data.json"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Font:
    default = pygame.font.Font("resources/fonts/acme.ttf", 32)
    daemon = pygame.font.Font("resources/fonts/daemon.ttf", 32)
    comfortaa = pygame.font.Font("resources/fonts/comfortaa.ttf", 32)
    title_logo = pygame.font.Font("resources/fonts/acme.ttf", 72)
    acme = pygame.freetype.Font("resources/fonts/acme.ttf", 32)
    pixel = pygame.freetype.Font("resources/fonts/pixel.ttf", 32)


Font.default = Font.pixel


class Color:
    BACKGROUND = hex_to_rgb("#06181E")  # Background Color
    TEXT_BACKGROUND = hex_to_rgb("#460D3A")  # Text Background
    TEXT_COLOR = hex_to_rgb("#FFFFFF")  # Normal Text Color
    TEXT_INVERSE = hex_to_rgb("#00000")  # Inverted Text Color
    TEXT_RED = hex_to_rgb("#FF0000")  # Names are red
    TEXT_GREEN = hex_to_rgb("#00FF00")  # Places are green
    TEXT_BLUE = hex_to_rgb("#0000FF")  # Things are blue
    BORDER_ONE = hex_to_rgb("#0ED1F0")  # Border Color One
    BORDER_TWO = hex_to_rgb("#F0CD00")  # Border Color Two

    @staticmethod
    def random_color():
        return (
            int(randrange(0, 255)),
            int(randrange(0, 255)),
            int(randrange(0, 255)),
        )
