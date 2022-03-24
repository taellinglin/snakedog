import pygame
import logging

from config import Color, Font


class Button(pygame.Surface):
    """
    Center text by default
    """

    def __init__(
        self,
        width,
        height,
        inner_text="Button",
        text_color=None,
        font=None,
        button_name=None,
        button_group=None,
    ):
        super().__init__((width, height), pygame.SRCALPHA)

        self.width, self.height = width, height
        self.text_color = text_color or Color.TEXT_COLOR
        self.font = font or Font.default
        self.text = inner_text
        self.selected = False

        self.button_name = button_name or "Unnamed button"

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = " ".join(list(value))
        self.fw, self.fh = self.font.size(self.text)

    def press(self):
        logging.info(f"Button {self.button_name} pressed")

    def update(self):
        self.fill((0, 0, 0, 0))

        text = self.font.render(
            self.text,
            True,
            self.text_color,
        )

        font_rect = pygame.Rect(0, 0, self.fw, self.fh)
        font_rect.center = self.get_rect().center

        if self.selected:
            surf = pygame.Surface((60, 60))
            surf.fill((255, 255, 255))
            rect = pygame.Rect(0, 0, 60, 60)
            rect.right = font_rect.left
            rect.centery = font_rect.centery
            self.blit(surf, rect)

        self.blit(text, font_rect)
