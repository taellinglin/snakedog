from turtle import Vec2D, pos
import pygame
import engine
from .scene import BaseScene
from config import Fonts
from components import Grid, Tile
from engine.map import Map


class Tutorial(BaseScene):
    def __init__(self, game, screen):
        super().__init__(game)
        # Create gruop of tiles for this layer
        self.tiles = pygame.sprite.Group()
        self.map = Map(self.tiles, pygame.Vector2(64 * 8, 64 * 4))
        self.screen = screen

    def render(self):
        self.map.runLogic()
        # self.map.processEvents()
        self.map.draw(self.screen)
        self.map.player.update()
        pass

    def event(self, event):
        if event.type == pygame.QUIT:
            return True
        # Get keyboard input and move player accordingly
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.map.player.goLeft()
            elif event.key == pygame.K_RIGHT:
                self.map.player.goRight()
            elif event.key == pygame.K_UP:
                self.map.player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.map.player.changeX < 0:
                self.map.player.stop()
            elif event.key == pygame.K_RIGHT and self.map.player.changeX > 0:
                self.map.player.stop()
