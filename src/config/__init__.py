# setup stuff here

import logging
from enum import Enum

import pygame

pygame.init()
pygame.font.init()

logging.basicConfig(filename="game.debug.log", level=logging.DEBUG, filemode="w")
logging.info("loaded logger from config")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# TODO
# Fill out these classes


class Font:
    default = pygame.font.Font("freesansbold.ttf", 32)


class Color:
    pass
