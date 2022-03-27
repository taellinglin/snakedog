import json
import logging

import pygame

import config
import scenes
from music import Music
from animations import Shake, Bounce
from config import Color


class Game:
    def __init__(self):
        logging.info("Starting game object initialization")
        # Inject self
        pygame.game = self
        self.running = False
        # screen has to be loaded first because of some
        # utilities we are using
        self.screen = config.screen
        # current game fps
        self.fps = None

        # Add many more screens later
        class Scenes(object):
            # titlescreen = scenes.TitleScreen(self)
            start_screen = scenes.StartScreen(self)
            menu = scenes.Menu(self)
            game_scene = scenes.GameScene(self)
            level_select = scenes.LevelSelect(self)
            uitest = scenes.UITest(self)

        self.scenes = Scenes()

        self.hotkeys = [
            self.scenes.start_screen,
            self.scenes.menu,
            self.scenes.game_scene,
            self.scenes.level_select,
            self.scenes.uitest,
        ]

        class Animations(object):
            bounce = Bounce(120, 0, 20)
            shake = Shake(-5, 5)
            pass

        self.animations = Animations()

        # set first scene
        self.scene = self.scenes.game_scene

        self.level = 0
        self.clock = pygame.time.Clock()

        logging.info("loading game save file")
        self.game_save_file = GameSaveFile(config.SAVE_FILE)

        logging.info("Finished game object initialization")

    def update_animations(self):
        # Have to manually enumerate animations and add conditions
        self.animations.bounce.update()
        self.animations.shake.update()

    def main(self):
        """
        Blocking entry point for the entire game
        """
        logging.info("Staring main game loop")

        self.running = True

        Music.play_bgm("resources/audio/music/JazzPad.ogg", 0.2)

        while self.running:
            self.fps = self.clock.get_fps()
            for event in pygame.event.get():
                if self.event(event):
                    continue
                if self.scene.event(event):
                    continue
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(Color.BACKGROUND)
            self.update_animations()
            self.scene.render()
            self.draw_fps()
            pygame.display.update()
            self.clock.tick(60)

        logging.info("Attempting to save game")
        self.game_save_file.save()
        logging.info("Game saved")
        logging.info("Main game loop terminated successfully")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        logging.info(f"setting level to {level}")
        self.scenes.game_scene.level = level
        self._level = level

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if config.CHEATS:
                if event.key == pygame.K_F1:
                    self.scene = self.scenes.start_screen
                    return True
                if event.key == pygame.K_F2:
                    self.scene = self.scenes.menu
                    return True
                if event.key == pygame.K_F3:
                    self.scene = self.scenes.game_scene
                    return True
                if event.key == pygame.K_F4:
                    self.scene = self.scenes.level_select
                    return True
                if event.key == pygame.K_F5:
                    self.scene = self.scenes.uitest
                    return True
                if event.unicode.isdigit():
                    self.level = int(event.unicode)
                    self.scene = self.scenes.game_scene
                    return True

    def draw_fps(self):
        fps_text = config.Font.default.render(
            "FPS: " + str(int(self.fps)),
            Color.TEXT_COLOR,
            size=12,
        )

        self.screen.blit(fps_text[0], (fps_text[1].left, 12 - fps_text[1].top))


class GameSaveFile:
    """
    None stands for not loaded yet
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.load()

    @staticmethod
    def backup(self):
        with open(self.filename + ".errorbackup.json", "w+") as f:
            with open(self.filename, "r") as f2:
                f.write(f2.read())

    def load(self):
        with open(self.filename, "a+") as f:
            pass
        with open(self.filename, "r") as f:
            ctx = f.read()
            logging.info(f"loaded game save file: {ctx}")
            if ctx == "":
                logging.info("Game save file is empty. Generating new one...")
                self.reset()
                return
            self.data = json.loads(ctx)

    def reset(self):
        self.data = {
            "level_status": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ]
        }

    def save(self, data=None):
        data = data or self.data
        with open(self.filename, "w") as f:
            json.dump(data, f)
