import pygame
import os
import logging
import itertools
import re


class ResourceManager:
    __organization_regex = re.compile(r"^(.+?)(?:_(\d+))?\.\w+$")
    __invalid_index_exception = Exception("Invalid image index")

    def __init__(self, folder, fallback=None, loader_func=None):
        if not loader_func:
            raise Exception("loader_func is required")
        if fallback:
            if isinstance(fallback, str):
                fallback = loader_func(os.path.join(folder, fallback))

        gen = None
        try:
            gen = next(os.walk(folder))
        except StopIteration:
            raise Exception(f"This folder does not exist {folder}")
        folders = gen[1]
        files = gen[2]

        for path in folders:
            self.__setattr__(
                path,
                ResourceManager(
                    os.path.join(folder, path), fallback, loader_func=loader_func
                ),
            )

        file_groups = [
            m
            for name in files
            if (m := re.match(self.__organization_regex, name))
            or logging.error(f"{folder} -> {name} is not valid. Ignoring...")
        ]

        for key, group in itertools.groupby(file_groups, lambda x: x.group(1)):
            matches = list(group)
            count = len(matches)
            if count == 0:
                continue
            elif count == 1:
                match = matches[0]
                self.__setattr__(key, loader_func(os.path.join(folder, match.group(0))))
            else:
                l = [
                    self.__invalid_index_exception
                    for _ in range(max(int(m.group(2)) for m in matches) + 1)
                ]
                self.__setattr__(key, l)
                for match in matches:
                    l[int(match.group(2))] = loader_func(
                        os.path.join(folder, match.group(0))
                    )


class ImageManager(ResourceManager):
    def __init__(self, folder, fallback=None):
        super().__init__(folder, fallback, loader_func=pygame.image.load)


# images = ImageManager("resources/images")

# print(images.sprites.number_tile)
