import os
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

    def add_resource(self, name, resource):
        self.resources[name] = resource

    def get_resource(self, name):
        return self.resources[name]

    def resolve_path(self, path):
        return os.path.join("../", self.basepath, path)


class ImageManager(ResourceManager):
    def add_resources(self, name, resource):
        super().add_resource(name, pygame.image.load(self.resolve_path(resource)))


class AudioManager(ResourceManager):
    def add_resources(self, name, resource):
        super().add_resource(name, pygame.image.load(self.resolve_path(resource)))


# Export

AudioManager()
ImageManager()

audioManager = AudioManager.instance
imageManager = ImageManager.instance
