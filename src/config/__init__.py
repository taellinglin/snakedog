# setup stuff here

import logging
from enum import Enum

import pygame

logging.basicConfig(filename="game.debug.log", level=logging.DEBUG)
logging.info("loaded logger from config")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Fonts(Enum):
    default = pygame.font.Font("freesansbold.ttf", 32)
