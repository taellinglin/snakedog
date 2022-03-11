import pygame 
from bgm import bgm

music = bgm
music.playBgm('Hikari.ogg', 1)
pygame.init()
pygame.display.set_caption('Team SnakeDog')  
img = pygame.image.load('gfx/Rings.png') 
img = pygame.transform.scale(img,(1920,1080))
display = pygame.display.set_mode((1920,1080))
display.blit(img,[0,0])
pygame.display.update() 
while True:
  pass