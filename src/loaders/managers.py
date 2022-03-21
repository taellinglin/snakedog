import os
import logging

import pygame

from util import Singleton


class ResourceManager(Singleton):
    """
    Resource manager
    """

    def __init__(self, basepath):
        super().__init__()
        self.basepath = basepath
        self.resources = {}
        self.fallbacked = {}

    def add_resource(self, name, resource):
        self.resources[name] = resource

    def get_resource(self, name):
        r = self.resources.get(name, None)
        if r:
            return r
        if not self.fallbacked.get(name, False):
            logging.debug(
                f"Resource with name {name} was not found. Falling back to default."
            )
            self.fallbacked[name] = True
        return self.fallback

    def resolve_path(self, path):
        return os.path.join("./", self.basepath, path)


class ImageManager(ResourceManager):
    def __init__(self, base, fallback):
        super().__init__(base)
        logging.debug("initialized image manager")
        self.fallback = pygame.image.load(self.resolve_path(fallback))

    def add_resource(self, name, resource):
        logging.debug(f"Adding resource: {name}")
        super().add_resource(name, pygame.image.load(self.resolve_path(resource)))


class AudioManager(ResourceManager):
    def add_resource(self, name, resource):
        super().add_resource(name, pygame.image.load(self.resolve_path(resource)))
