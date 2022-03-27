import logging

import pygame

from render import WorldRender
from config import Font
from managers import ui as ui_components
import keyboard
from ui import ImageButton, BaseText
from .scene import BaseScene


class GameScene(BaseScene):
    """
    Change level to load a new world render
    """

    def __init__(self, game):
        super().__init__(game)
        self._level = None
        self.world_render = None
        self.menu_focus = False
        self.dim_screen = pygame.Surface(self.game.screen.get_size(), pygame.SRCALPHA)
        self.dim_screen.fill((0, 0, 0, 128))

        self.select_blink_timer = 0

        def go_to_level_select():
            self.game.scene = self.game.scenes.level_select

        def skip_level():
            self.game.scene = self.game.scenes.level_select
            self.game.game_save_file.data["level_status"][self.level] = True

        def close_menu():
            pass

        self.buttons = [
            ImageButton(
                ui_components.green_button_large,
                inner_text="Level Select",
                font=Font.default,
                scale=4,
                font_size=24,
                executor=go_to_level_select,
            ),
            ImageButton(
                ui_components.green_button_large,
                inner_text="Skip Level",
                font=Font.default,
                scale=4,
                font_size=24,
                executor=skip_level,
            ),
            ImageButton(
                ui_components.green_button_large,
                inner_text="Back (Esc)",
                font=Font.default,
                scale=4,
                font_size=24,
                executor=close_menu,
            ),
        ]

        self.moves_left = BaseText("      ", size=18)
        self.time_flow = BaseText("              ", size=18)
        self.moves_counter = BaseText("         ", size=18)

        self.button_selection_index = 0

    # This property is always in sync with game.level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        # world_render setting logic
        self._level = level
        if level is None:
            self.world_render = None
        else:
            self.world_render = WorldRender(self.game, level)

    def render(self):
        world = self.world_render.world

        if not world:
            self.game.scene = self.game.scenes.level_select
            return

        self.moves_left.text = (
            f"Moves Left: {world.total_moves - world.moves}/{world.total_moves}"
        )

        self.time_flow.text = "Timeflow: >>>" if world.flow == 1 else "Timeflow: <<<"
        self.moves_counter.text = f"At move: {world.action_index}"

        for idx, text in enumerate(
            [self.moves_left, self.time_flow, self.moves_counter]
        ):
            text.blit_to(
                self.game.screen,
                pygame.Vector2(0, 50) + pygame.Vector2(0, text.get_rect().height) * idx,
            )

        if self.select_blink_timer > 0:
            self.select_blink_timer -= 1
            if self.select_blink_timer == 0:
                self.menu_focus = False
                self.button_selection_index = 0
                self.buttons[self.button_selection_index].press()

        if world.gameover:
            if world.won:
                self.game.game_save_file.data["level_status"][self.level] = True
                self.game.scene = self.game.scenes.level_select
            else:
                world.shake_screen()
                world.reset()

        self.world_render.render_to(self.game.screen)
        if self.menu_focus:
            self.game.screen.blit(self.dim_screen, (0, 0))

            starting_point = self.game.screen.get_size()[1] - len(self.buttons) * (
                self.buttons[0].get_size()[1] + 30
            )

            for idx, button in enumerate(self.buttons):
                button.update()
                button.selected = (
                    idx == self.button_selection_index
                    and self.select_blink_timer % 10 < 5
                )
                self.game.screen.blit(
                    button,
                    (
                        self.game.screen.get_size()[0] - button.get_size()[0] - 30,
                        starting_point + idx * (button.get_size()[1] + 30),
                    ),
                )

    def event(self, e):
        if self.select_blink_timer:
            return True
        if self.menu_focus:
            if keyboard.is_select(e):
                self.select_blink_timer = 60
                return True
            if dxdy := keyboard.pygame_event_to_dxdy(e):
                _, dy = dxdy
                if dy != 0:
                    self.button_selection_index += dy
                    self.button_selection_index %= len(self.buttons)
                    return True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    logging.info("Closed menu")
                    self.button_selection_index = 0
                    self.menu_focus = False
                    return True
            return
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                logging.info("Opened menu")
                self.menu_focus = True
            if e.key == pygame.K_r:
                self.world_render.world.shake_screen()
                self.world_render.world.reset()
        self.world_render.event(e)
