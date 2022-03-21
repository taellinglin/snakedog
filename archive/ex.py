#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("game base")
screen = pygame.display.set_mode((500, 500), 0, 32)

# make sure you provide your own image
img = pygame.image.load("img1.png").convert()
img.set_colorkey((0, 0, 0))

angle = 0
# Loop ------------------------------------------------------- #
while True:
    angle += 6

    # Background --------------------------------------------- #
    screen.fill((0, 50, 0))

    mx, my = pygame.mouse.get_pos()
    img_copy = pygame.transform.rotate(img, angle)
    screen.blit(
        img_copy,
        (mx - int(img_copy.get_width() / 2), my - int(img_copy.get_height() / 2)),
    )

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
