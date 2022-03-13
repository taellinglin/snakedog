import pygame
import os

# import sf2_loader
from bgm import bgm
from lasso import lasso
from random import choice
from simplemidi import simplemidi

soundfonts = lasso.load("sf2/", ".sf2")  # SF2
midifiles = lasso.load("midi/", ".mid")  # MIDI
xmfiles = lasso.load("xm/", ".xm")  # XM
soundtrack = lasso.load("bgm/", ".ogg")  # OGG
soundtrackhq = lasso.load("bgmhq/", ".wav")  # Stereo WAV
soundfx = lasso.load("sfx/", ".wav")  # Stereo WAV
soundfx3d = lasso.load("sfx3d/", ".wav")  # Mono WAV
sm = simplemidi
music = bgm
selected_track = choice(
    soundtrack + midifiles + xmfiles
)  # Change to soundtrackhq for studio quality
# sm.playmidi(choice(midifiles), choice(soundfonts))
music.playBgm(selected_track, 1)
pygame.init()
pygame.display.set_caption("Team SnakeDog")
img = pygame.image.load("gfx/Rings.png")
img = pygame.transform.scale(img, (1920, 1080))
display = pygame.display.set_mode((1920, 1080))
display.blit(img, [0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    pygame.time.Clock().tick(60)
