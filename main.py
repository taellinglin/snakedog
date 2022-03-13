import pygame
from bgm import bgm

music = bgm
music.playBgm("Hikari.ogg", 1)
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
