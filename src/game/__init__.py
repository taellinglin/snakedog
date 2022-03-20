class Game:
    def __init__(self):
        pass

    def tick(self):
        pass


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for x in range(width)] for y in range(height)]

    def check(self, x, y):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return True
        raise Exception("Invalid cell coordinates")

    def set_cell(self, x, y, cell):
        self.check(x, y)
        self.grid[y][x] = cell

    def get_cell(self, x, y):
        self.check(x, y)
        return self.grid[y][x]


class BaseTile:
    def __init__(self):
        pass


class TileEntity(BaseTile):
    def __init__(self):
        super().__init__()


class Tile(BaseTile):
    def __init__(self):
        super().__init__()
