import math

from .animation import BaseAnimation


class Bounce(BaseAnimation):
    def __init__(self, loop, low, high):
        def func(clock):
            return int(low + (high - low) * abs(math.sin(2 * math.pi * clock / loop)))

        super().__init__(func=func)
