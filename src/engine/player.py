
import pygame
from engine.spritesheet import SpriteSheet
from config import MAP_COLLISION_LAYER
from config import SCREEN_HEIGHT
from config import SCREEN_WIDTH
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #Load the spritesheet of frames for this player
        self.sprites = SpriteSheet("resources/images/sprites/player.png")
    
        self.stillRight = self.sprites.image_at((0, 0, 30, 42))
        self.stillLeft = self.sprites.image_at((0, 42, 30, 42))
        
        #List of frames for each animation
        self.runningRight = (self.sprites.image_at((0, 84, 30, 42)),
                    self.sprites.image_at((30, 84, 30, 42)),
                    self.sprites.image_at((60, 84, 30, 42)),
                    self.sprites.image_at((90, 84, 30, 42)),
                    self.sprites.image_at((120, 84, 30, 42)))

        self.runningLeft = (self.sprites.image_at((0, 126, 30, 42)),
                    self.sprites.image_at((30, 126, 30, 42)),
                    self.sprites.image_at((60, 126, 30, 42)),
                    self.sprites.image_at((90, 126, 30, 42)),
                    self.sprites.image_at((120, 126, 30, 42)))
                    
        self.jumpingRight = (self.sprites.image_at((30, 0, 30, 42)),
                    self.sprites.image_at((60, 0, 30, 42)),
                    self.sprites.image_at((90, 0, 30, 42)))

        self.jumpingLeft = (self.sprites.image_at((30, 42, 30, 42)),
                    self.sprites.image_at((60, 42, 30, 42)),
                    self.sprites.image_at((90, 42, 30, 42)))
        
        self.image = self.stillRight
        
        #Set player position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        #Set speed and direction
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
        #Boolean to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()
        
        #Players current level, set after object initialized in game constructor
        self.currentLevel = None
        
    def update(self):
        #Update player position by change
        self.rect.x += self.changeX
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        
        #Move player to correct side of that block
        for tile in tileHitList:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right
            if self.changeY > 0:
                self.rect.bottom = tile.rect.top
            else:
                self.rect.top = tile.rect.bottom
        #Move screen if player reaches screen bounds
        if self.rect.right >= SCREEN_WIDTH - 600:
            difference = self.rect.right - (SCREEN_WIDTH - 600)
            self.rect.right = SCREEN_WIDTH - 600
            self.currentLevel.shiftLevel(-difference, 0)
        
        #Move screen is player reaches screen bounds
        if self.rect.left <= 600:
            difference = 600 - self.rect.left
            self.rect.left = 600
            self.currentLevel.shiftLevel(difference, 0)
        
        if self.rect.bottom >= SCREEN_HEIGHT - 400:
            difference = self.rect.bottom - (SCREEN_HEIGHT - 400)
            self.rect.bottom = SCREEN_HEIGHT - 400
            self.currentLevel.shiftLevel(0,-difference)
        
        #Move screen is player reaches screen bounds
        if self.rect.top <= 400:
            difference = 400 - self.rect.top
            self.rect.top = 400
            self.currentLevel.shiftLevel(0, difference)
        #Update player position by change
        self.rect.y += self.changeY
        self.rect.x += self.changeX
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
       
        #If there are tiles in that list
        if len(tileHitList) > 0:
            #Move player to correct side of that tile, update player frame
            for tile in tileHitList:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1
                    
                    if self.direction == "right":
                        self.image = self.stillRight
                    else:
                        self.image = self.stillLeft
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        #If there are not tiles in that list
        else:
            #Update player change for jumping/falling and player frame
            self.changeY += 0.2
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[1]
                else:
                    self.image = self.jumpingLeft[1]
        
        #If player is on ground and running, update running animation
        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.runningRight[self.runningFrame]
            else:
                self.image = self.runningLeft[self.runningFrame]
        
        #When correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 4:
                self.runningFrame = 0
            else:
                self.runningFrame += 1
    
    #Make player jump
    def jump(self):
        #Check if player is on ground
        self.rect.y += 2
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 2
        
        if len(tileHitList) > 0:
            if self.direction == "right":
                self.image = self.jumpingRight[0]
            else:
                self.image = self.jumpingLeft[0]
                
            self.changeY = -10
    
    #Move right
    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 3
    
    #Move left
    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -3
    
    #Stop moving
    def stop(self):
        self.running = False
        self.changeX = 0
    
    #Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)