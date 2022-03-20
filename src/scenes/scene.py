from util import Singleton


class BaseScene(Singleton):
    """
    Base class for scenes to be written.

    Optionally implement `event()` and `render()` methods.
    """

    def __init__(self, game):
        self.game = game

    def event(self):
        pass

    def render(self):
        pass
