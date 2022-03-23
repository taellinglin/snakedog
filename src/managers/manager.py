import os
import logging
import itertools
import re
import inspect

import pygame

import util


class ResourceManager:
    __organization_regex = re.compile(r"^(.+?)(?:_(\d+))?\.(\w+)$")
    __invalid_index_exception = Exception("Invalid image index")

    def __init__(self, folder=None, fallback=None, loader_func=None):
        if not folder:
            # Blank instance
            return
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
            if path.startswith("__") and path.endswith("__"):
                continue
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
            if "py" in [m.group(3) for m in matches]:
                # There is a python file
                if len(matches) > 2:
                    raise Exception(f"{folder} -> {key} should only be a pair")

                resource_file_list = [m.group(0) for m in matches if m.group(3) != "py"]
                if not resource_file_list:
                    logging.info(
                        f"{folder} -> {key} has no resource file (no file of same name that doens't end with .py)"
                    )
                    continue

                resource_file = resource_file_list[0]

                datafile = util.load_module(os.path.join(folder, key + ".py"))

                if datafile.TYPE == "SPRITE":
                    # Deal with sprite logic
                    dimensions = datafile.DIMENSIONS
                    if not dimensions:
                        raise Exception("Sprite must have dimensions")

                    width, height = dimensions

                    data = datafile.data

                    if not data:
                        raise Exception("A sprite info file must have a class data")

                    image = loader_func(os.path.join(folder, resource_file))

                    store = type(self)()
                    self.__setattr__(key, store)

                    for attr, value in inspect.getmembers(
                        data, lambda a: not inspect.isroutine(a)
                    ):
                        if attr.startswith("__") and attr.endswith("__"):
                            continue

                        if not (isinstance(value, list) or isinstance(value, tuple)):
                            raise Exception(f"{attr} must be a list or tuple")

                        if len(value) < 2:
                            raise Exception(f"{attr} must have at least 2 elements")
                        elif len(value) == 2:
                            # tile at location
                            store.__setattr__(
                                attr,
                                util.splice_image(
                                    image, width, height, value[0], value[1]
                                ),
                            )
                        elif len(value) == 4:
                            # tile array
                            idx = 0
                            l = [
                                self.__invalid_index_exception
                                for i in range(
                                    (value[2] - value[0]) * (value[3] - value[1])
                                )
                            ]
                            for x in range(value[0], value[2]):
                                for y in range(value[1], value[3]):
                                    x_loc = x * width
                                    y_loc = y * height
                                    l[idx] = util.splice_image(
                                        image, width, height, x_loc, y_loc
                                    )
                                    idx += 1
                            store.__setattr__(
                                attr,
                                l,
                            )
                        else:
                            raise Exception(
                                f"{attr} must have either 2 (single tile) or 4 (array of elements)"
                            )
                else:
                    raise Exception(f"{datafile.TYPE} is not a valid resource type")
                continue

            count = len(matches)
            if count == 0:
                continue
            elif count == 1:
                match = matches[0]
                self.__setattr__(key, loader_func(os.path.join(folder, match.group(0))))
            else:
                l = [
                    self.__invalid_index_exception
                    for _ in range(
                        max(int(m.group(2)) for m in matches if m.group(2) is not None)
                        + 1
                    )
                ]
                self.__setattr__(key, l)
                for match in matches:
                    l[int(match.group(2))] = loader_func(
                        os.path.join(folder, match.group(0))
                    )


class ImageManager(ResourceManager):
    def __init__(self, folder, fallback=None):
        super().__init__(
            folder, fallback, loader_func=util.debug_arguments(pygame.image.load)
        )


class AudioManager(ResourceManager):
    pass
