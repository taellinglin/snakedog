import importlib.util as iu
import logging
import os

import pygame


def load_module(filepath):
    file = os.path.basename(filepath)
    spec = iu.spec_from_file_location(file, filepath)
    if not spec:
        raise ImportError(f"{filepath} is not a valid module")

    module = iu.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def splice_image(source_img, width, height, x, y):
    rect = pygame.Rect(0, 0, width, height)
    surf = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
    surf.blit(source_img, (0, 0), (x, y, x + width, y + height))
    return surf


def debug_arguments(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(e)
            logging.error(f"^ while calling {func.__name__}({args}, {kwargs})")

    return wrapper
