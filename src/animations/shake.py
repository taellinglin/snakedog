import random

from .animation import BaseAnimation


class Shake(BaseAnimation):
    def __init__(self, left, right):
        def func(clock):
            if clock % 3 == 0:
                return left + (right - left) * random.random()

        super().__init__(func=func)
