import pygame


class Tile:
    def __init__(self, column, row, x, y, width, height, typ=None):

        # the parameters that define how the tile is drawn
        self.color = (0, 0, 255)

        self.x = x
        self.y = y
        self.rect = (x, y, width, height)

        # this list will contain all of the objects that are currently on the tile
        self.contents = []

        # supported tile types, None = blank, "wall" = wall, add more also update translatingDict if you add more
        self.tileType = typ

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, width=1)


class Grid:
    def __init__(self, screen, rows, columns, grid_origin=(0, 0), tile_size=(100, 100)):

        # the number of total rows and columns in the grid
        self.rows = rows
        self.columns = columns

        # the width and hight of each tile
        tile_width = tile_size[0]
        tile_height = tile_size[1]

        # the pygame surface to draw the grid on
        self.screen = screen

        # tiles is a 2D list of tile objects
        self.tiles = [
            [
                Tile(
                    column,
                    row,
                    (column * tile_width) + grid_origin[0],
                    (row * tile_height) + grid_origin[1],
                    tile_width,
                    tile_height,
                )
                for row in range(rows)
            ]
            for column in range(columns)
        ]

    def draw(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.tiles[column][row].draw(self.screen)

    def returnGridRepr(self):
        translatingDict = {None: ".", "wall": "#"}
        grid = (
            {}
        )  # TODO ensure the outer edges of the grid are walls otherwise this will all break
        for row in range(self.rows):
            for column in range(self.columns):
                grid[(column, row)] = translatingDict[self.tiles[column][row].tileType]
                # takes the newest row adds the char repr of the tiletype
        return grid
