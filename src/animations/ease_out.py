import math

from .animation import BaseAnimation


class EaseOut(BaseAnimation):
    """
    0 to 1
    """

    def __init__(self, duration):
        def func(clock):
            return 1 - (self.clock / duration) ** 2

        super().__init__(func=func, loop=duration, once=True)
