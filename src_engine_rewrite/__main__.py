import pygame
import pytmx

pygame.init()

screen = pygame.display.set_mode((640, 480))

running = True

clock = pygame.time.Clock()

tile_image = pygame.image.load("resources/images/sprites/test-tile.png")
player_image = pygame.image.load("resources/images/sprites/test-tile.png")

tmx = pytmx.load_pygame("resources/maps/animation-test.tmx")

tile = pygame.sprite.Sprite()
tile.image = tile_image
tile.rect = tile_image.get_rect()
tile.color = (255, 255, 255)
tile.rect.x = 100

tile.update = lambda: screen.blit(tile.image, tile.rect)

player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player_image.get_rect()
player.color = (255, 0, 0)

player.update = lambda: screen.blit(player.image, player.rect)

sprites = [tile, player]

# pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

from pytmx.util_pygame import load_pygame
import pygame
import pyscroll
import time


class Sprite(pygame.sprite.Sprite):
    """
    Simple Sprite class for on-screen things

    """

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()


# Load TMX data
tmx_data = load_pygame("resources/maps/animation-test.tmx")

# Make the scrolling layer
map_layer = pyscroll.BufferedRenderer(
    pyscroll.TiledMapData(tmx_data),
    (400, 400),
    alpha=True,
)

# make the pygame SpriteGroup with a scrolling map
group = pyscroll.PyscrollGroup(map_layer)

# Add sprite(s) to the group
image = pygame.image.load("resources/images/sprites/test-tile.png").convert_alpha()
camera = Sprite(image)
group.add(camera)

# Center the camera on the sprite
group.center(camera.rect.center)

# Draw map and sprites using the group
# Notice I did not `screen.fill` here!  Clearing the screen is not
# needed since the map will clear it when drawn

bb = False

x = y = 0

map_layer.reload()

# map_layer.zoom -= 0.01

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                bb = not bb
            if e.key == pygame.K_f:
                map_layer.zoom += 0.01
            if e.key == pygame.K_g:
                map_layer.zoom -= 0.01

    if pygame.key.get_pressed()[pygame.K_d]:
        x += 10
    if pygame.key.get_pressed()[pygame.K_s]:
        y += 10
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 10
    if pygame.key.get_pressed()[pygame.K_w]:
        y -= 10

    # # game logic
    # camera.rect.x = x
    # camera.rect.y = y
    group.center((x, y))
    group.update()

    screen.fill(pygame.Color("white"))
    # screen.fill(pygame.Color("black"))

    # if bb:
    #     for i in sprites:
    #         pygame.draw.rect(screen, i.color, i.rect)
    # else:
    #     for i in sprites:
    #         i.update()

    group.draw(screen)

    screen.blit(player.image, (100, 100))

    pygame.display.flip()

    clock.tick(60)
