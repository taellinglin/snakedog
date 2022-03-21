import pygame
import random
import math

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont("Comic Sans MS", 30)


# Set up the drawing window
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])


enemies = []


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.1
        self.radius = 10
        self.health = 100

        self.image = pygame.transform.scale(pygame.image.load("img1.png"), (100, 100))

        self.color = (0, 0, 255)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def handle_input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            self.x += self.speed
        if pressed_keys[pygame.K_LEFT]:
            self.x -= self.speed
        if pressed_keys[pygame.K_UP]:
            self.y -= self.speed
        if pressed_keys[pygame.K_DOWN]:
            self.y += self.speed

    def check_collision(self):
        for enemy in enemies:
            if (
                self.x + self.radius >= enemy.x
                and self.x - self.radius <= enemy.x + enemy.w
            ):
                if (
                    self.y + self.radius >= enemy.y
                    and self.y - self.radius <= enemy.y + enemy.h
                ):
                    self.color = (255, 255, 0)
                    self.health -= 1
                    return

        self.color = (0, 0, 255)

    def check_alive_status(self):
        color = (0, 0, 0)

        if self.health <= 0:
            color = (255, 0, 0)

        text = myfont.render(str(self.health), False, color)
        screen.blit(text, (100, 100))

    def rotate(self):

        original_image = self.image
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y

        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        print(angle)

        self.image = pygame.transform.rotate(original_image, int(angle))
        self.rect = self.image.get_rect(center=(self.x, self.y))


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.w = 20
        self.h = 20

    def draw(self):
        pygame.draw.rect(screen, (155, 0, 155), (self.x, self.y, self.w, self.h))


player = Player(500, 200)


for i in range(0, 10):
    enemies.append(
        Enemy(random.randrange(0, screen_width), random.randrange(0, screen_height))
    )


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    player.handle_input()
    player.check_collision()
    player.rotate()
    player.draw()
    player.check_alive_status()
    for enemy in enemies:
        enemy.draw()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
