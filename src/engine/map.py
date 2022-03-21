import pygame
from engine.player import Player
from engine.level import Level
from config import Color


class Map(object):
    def __init__(self, tiles,startPos):
        #Set up a level to load
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(fileName = "resources/maps/test.tmx", tiles = tiles))
        self.currentLevel = self.levels[self.currentLevelNumber]
        
        #Create a player object and set the level it is in
        self.player = Player(startPos.x, startPos.y)
        self.player.currentLevel = self.currentLevel
        
        #Draw aesthetic overlay
        #self.overlay = pygame.image.load("resources/overlay.png")
        #Create gruop of tiles for this layer
        self.tiles = tiles
        
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            #Get keyboard input and move player accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()
            
        return False
        
    def runLogic(self):
        #Update player movement and collision logic
        self.player.update()
    
    #Draw level, player, overlay
    def draw(self, screen):
        screen.fill(Color.BACKGROUND)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        #screen.blit(self.overlay, [0, 0])
        pygame.display.flip()