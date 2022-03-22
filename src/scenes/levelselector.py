from typing import Collection
from .scene import BaseScene
import pygame
from config import Color, Fonts


class LevelSelect(BaseScene):
    def __init__(self, game):
        print(type(game))
        super().__init__(game)
        self.font = Fonts.default
        self.curPos = [0, 0]
        self.levels = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.levelpos = []
        i, j = 0, 0
        for item in self.levels:  # one level

            self.levelpos.append([])
            for level in item:  # 2 level

                level = self.font.render(
                    str(level), True, Color.TEXT_COLOR, Color.BACKGROUND
                )
                levelpos = (30 + i * 50, 30 + j * 30)
                level_rect = level.get_rect()
                level_rect.center = levelpos
                self.levelpos[-1].append(levelpos)
                self.game.screen.blit(level, level_rect)
                j += 1
            i += 1
            j = 0

    def adjustpos(self, i, di: int):
        if self.curPos[i] + di < 0:  # checking negative overflow
            self.curPos[i] = len(self.levels if i == 0 else self.levels[i]) - 1
        elif self.curPos[i] + di == len(
            self.levels if i == 0 else self.levels[i]
        ):  # checking if pos overflow
            self.curPos[i] = 0
        else:
            self.curPos[i] += di

    def render(self):
        i, j = 0, 0
        for item in self.levels:  # one level

            self.levelpos.append([])
            for level in item:  # 2 level

                level = self.font.render(
                    str(level),
                    True,
                    Color.TEXT_COLOR,
                    Color.BACKGROUND if not [j, i] == self.curPos else Color.TEXT_BLUE,
                )
                levelpos = (30 + i * 50, 30 + j * 30)
                level_rect = level.get_rect()
                level_rect.center = levelpos
                self.levelpos[-1].append([level, levelpos])
                self.game.screen.blit(level, level_rect)
                j += 1
            i += 1
            j = 0

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            # 119 W,         97 A,            115 S,           100 D
            # 1073741906 up, 1073741904 left, 1073741905 down, 1073741903 right
            if event.key == 13:  # enter
                pass
                #  self.game.scene = self.game.scenes.levels.levelselected
            elif event.key in (119, 1073741906):  # move cur up
                self.adjustpos(0, -1)
            elif event.key in (97, 1073741904):  # move cur left
                self.adjustpos(1, -1)
            elif event.key in (115, 1073741905):  # move cur down
                self.adjustpos(0, 1)
            elif event.key in (100, 1073741903):  # move cur right
                self.adjustpos(1, 1)
