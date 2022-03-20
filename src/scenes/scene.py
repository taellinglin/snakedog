from util import Singleton


class BaseScene(Singleton):
    """
    Base class for scenes to be written.

    Optionally implement `tick()` and `render()` methods.
    """

    def __init__(self, game):
        self.game = game

    def tick(self):
        pass

    def render(self):
        pass
