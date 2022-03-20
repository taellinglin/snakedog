class SingleTon:
    """
    Singleton class
    """

    instance = None

    def __init__(self):
        if type(self).instance is not None:
            raise Exception("This class is a singleton!")
        type(self).instance = self
