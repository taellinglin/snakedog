import pygame
import os

# import sf2_loader
from bgm import bgm
from lasso import lasso
from random import choice
from simplemidi import simplemidi

# import the grid classes
from grid import Grid, Tile

soundfonts = lasso.load("sf2/", ".sf2")  # SF2
midifiles = lasso.load("midi/", ".mid")  # MIDI
xmfiles = lasso.load("xm/", ".xm")  # XM
soundtrack = lasso.load("bgm/", ".ogg")  # OGG
soundtrackhq = lasso.load("bgmhq/", ".wav")  # Stereo WAV
soundfx = lasso.load("sfx/", ".wav")  # Stereo WAV
soundfx3d = lasso.load("sfx3d/", ".wav")  # Mono WAV
sm = simplemidi
music = bgm
selected_track = choice(soundtrack + midifiles + xmfiles)
# Change choice(soundtrack... to choice(soundtrackhq... for studio quality
# sm.playmidi(choice(midifiles), choice(soundfonts))


pygame.init()
pygame.display.set_caption("Team SnakeDog")
screen_width = 1920
screen_height = 1080

# Play BGM
music.playBgm(selected_track, 1, True)

# img = pygame.image.load("gfx/Rings.png")
# img = pygame.transform.scale(img, (1920, 1080))
display = pygame.display.set_mode((screen_width, screen_height))
# display.blit(img, [0, 0])

grid = Grid(
    display,
    9,
    16,
    grid_origin=(screen_width / 6, screen_height / 6),
    tile_size=(75, 75),
)

# the main draw function where all other classes are drawn
def draw():
    # clear the screen
    display.fill((255, 255, 255))
    grid.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw()

    pygame.display.update()
    pygame.time.Clock().tick(60)
