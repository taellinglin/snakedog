import pygame
import os
#import sf2_loader
from bgm import bgm
from lasso import lasso
from random import choice

soundfonts = lasso.load('sf2/','.sf2') # SF2 
midifiles = lasso.load('midi/','.mid') # MIDI
soundtrack = lasso.load('bgm/','.ogg') # OGG
soundtrackhq = lasso.load('bgmhq/','.wav') # Stereo WAV
soundfx = lasso.load('sfx/','.wav') # Stereo WAV
soundfx3d = lasso.load('sfx3d/','.wav') # Mono WAV
music = bgm
music.playBgm(choice(soundtrack+midifiles), 1)
pygame.init()
pygame.display.set_caption('Team SnakeDog')  
img = pygame.image.load('gfx/Rings.png') 
img = pygame.transform.scale(img,(1920,1080))
display = pygame.display.set_mode((1920,1080))
display.blit(img,[0,0])
pygame.display.update() 
while True:
  pass