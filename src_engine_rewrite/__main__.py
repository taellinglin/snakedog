import pygame
import pytmx
import random

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

running = True

clock = pygame.time.Clock()

# tile_image = pygame.image.load("resources/images/sprites/test-tile.png")
# player_image = pygame.image.load("resources/images/sprites/test-tile.png")

# tmx = pytmx.load_pygame("resources/maps/animation-test.tmx")

# tile = pygame.sprite.Sprite()
# tile.image = tile_image
# tile.rect = tile_image.get_rect()
# tile.color = (255, 255, 255)
# tile.rect.x = 100

# tile.update = lambda: screen.blit(tile.image, tile.rect)

# player = pygame.sprite.Sprite()
# player.image = player_image
# player.rect = player_image.get_rect()
# player.color = (255, 0, 0)

# player.update = lambda: screen.blit(player.image, player.rect)

# sprites = [tile, player]

# pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

from pytmx.util_pygame import load_pygame
import pygame
import pyscroll
import time

from img import ImageManager

images = ImageManager("resources/images")


def keyboard_to_dxdy(e):
    if e.type != pygame.KEYDOWN:
        return (0, 0)
    return (
        {
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0),
        }
    ).get(e.key, (0, 0))


class TileAlignedEntity(pygame.sprite.Sprite):
    """
    Does not handle rect logic after initialization
    """

    def __init__(
        self,
        image,
        position,
        clock_loop=0,
        images=None,
        smooth_move_animation=False,
        z=0,
        is_wall=False,
    ):
        super().__init__()
        self.z = z
        self.is_wall = is_wall
        self.world = None
        self.image = image
        self.images = images

        if not image:
            raise Exception("Base image required for bounding box calculation")

        self.rect = image.get_rect()

        self.render_loc = pygame.Vector2(self.rect.x, self.rect.y)

        self.col, self.row = position

        self.clock = 0
        self.clock_loop = clock_loop

        self.smooth_move_animation = smooth_move_animation

    def post_init(self):
        self.world._update_sprite_rect(self)
        self.reset_smooth_move_animation()

    def update(self):
        """
        This should only be called after the rect has been adjusted by the world
        """
        # update clock
        self.clock = (
            (1 + self.clock) % self.clock_loop
            if self.clock_loop > 0
            else self.clock + 1
        )

        self._update_image()

        if self.smooth_move_animation:
            self.render_loc = 0.8 * self.render_loc + 0.2 * pygame.Vector2(
                self.rect.x, self.rect.y
            )
            self.world.surface.blit(self.image, self.render_loc)
        else:
            # this should be called after the rect has been adjusted by the world
            self.world.surface.blit(self.image, self.rect)
            pass

    def _update_image(self):
        pass

    def reset_smooth_move_animation(self):
        self.render_loc = pygame.Vector2(self.rect.x, self.rect.y)

    def reset_clock_loop(self, clock_loop):
        """
        This will be useful for handling animations
        """
        self.clock_loop = clock_loop
        self.clock = 0

    def get_collided_sprites(self):
        return [
            e
            for e in pygame.sprite.spritecollide(self, self.world.sprites(), False)
            if e is not self
        ]

    def event(self, event):
        pass

    def push_to(self, col, row=None, **kwargs):
        if not row:
            col, row = col
        return False


class Box(TileAlignedEntity):
    def push_to(self, direction, reversed=False):
        potential_wall = self.world.tile_at(
            self.col + direction[0], self.row + direction[1]
        )
        if potential_wall:
            return False
        potential_box = self.world.entity_at(
            self.col + direction[0], self.row + direction[1]
        )
        if potential_box:
            if not isinstance(potential_box, TileAlignedEntity):
                # We don't know what this is
                return False

            if potential_box.is_wall:
                return False

            # push the box too
            if not potential_box.push_to(direction):
                return False
        # There is nothing. Update position
        self.col += direction[0]
        self.row += direction[1]
        return True


class Player(TileAlignedEntity):
    def __init__(self, *args, **kwargs):
        if "z" not in kwargs:
            kwargs["z"] = 999
        super().__init__(*args, **kwargs)
        self.push_frames = 0

    def event(self, event):
        dx, dy = keyboard_to_dxdy(event)
        if dx or dy:
            nx, ny = self.col + dx, self.row + dy
            if not self.world.is_wall(nx, ny):
                entity = self.world.entity_at(nx, ny)
                if entity:
                    if isinstance(entity, Box):
                        if entity.push_to((dx, dy)):
                            self.push_frames = 30
                        else:
                            return
                    if entity.is_wall:
                        return
                self.col, self.row = nx, ny
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Check collisions from tile
                tile = self.world.tile_at(self.col, self.row)
                # Check collisions from entity
                entities = self.get_collided_sprites()
                for entity in entities:
                    if isinstance(entity, Switch):
                        entity.toggle()
                pass

    def _update_image(self):
        self.push_frames -= 1
        if self.push_frames > 0:
            self.image = self.images.player_stick_push
        else:
            self.image = self.images.player_stick


class Switch(TileAlignedEntity):
    def __init__(self, *args, on_update=lambda _: _, on=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.on = on
        self.on_update = on_update

    def toggle(self, reversed=False):
        self.on = not self.on
        self.on_update(self.on)

    def _update_image(self):
        self.image = self.images.switch_on if self.on else self.images.switch_off


class Door(TileAlignedEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.open = False

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self.is_wall = not value
        self._open = value

    def _update_image(self):
        self.image = self.images.door_open if self.open else self.images.door_closed


class World(pygame.sprite.Group):
    def __init__(
        self, filename, dimensions, offset=(0, 0), entity_loader_func=None, moves=10
    ):
        super().__init__()

        self.moves = moves
        self.total_moves = moves
        self.gameover = False
        self.flow = 1

        self.player = None
        self.ghost = None

        self.tmx_data = pytmx.util_pygame.load_pygame(filename)
        self.map_layer = pyscroll.BufferedRenderer(
            pyscroll.TiledMapData(self.tmx_data),
            dimensions,
            alpha=True,
        )
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        # create a new surface of dimensions so it matches the map layer
        self.surface = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        self.pyscroll_group = pyscroll.PyscrollGroup(self.map_layer)

        self.offset = offset
        self.entity_loader_func = entity_loader_func
        self.reset()

        for id, layer in enumerate(self.tmx_data.layers):
            if "collision" in layer.name:
                self.primary_collision_layer_id = id
                break
        else:
            raise Exception("No collision layer found")

    def tile_at(self, col, row):
        return self.tmx_data.get_tile_image(col, row, self.primary_collision_layer_id)

    def tile_at_layer(self, col, row, layer):
        return self.tmx_data.get_tile_image(col, row, layer)

    def entity_at(self, col, row):
        for sprite in self.sprites():
            if sprite.col == col and sprite.row == row:
                return sprite
        return None

    def reverse_flow(self):
        if self.flow == -1:
            raise Exception("Flow already reversed")
        self.flow = -1

    def commit_action(self, reverse_action):
        """
        Removes 1 move from self.moves

        Must provide the reverse_action for the action that happened
        """
        if self.flow == -1:
            self.moves -= 1
        else:
            self.moves -= 1
            if self.moves == 0:
                self.gameover = True
            self.actions[self.moves] = reverse_action

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, val):
        self._offset = val

    def update(self):
        # update all entities
        for sprite in sorted(
            self.sprites(), key=lambda s: getattr(s, "z", 0) if s else 0
        ):
            if isinstance(sprite, TileAlignedEntity):
                self._update_sprite_rect(sprite)
            sprite.update()

    def _update_sprite_rect(self, sprite):
        # update their rect
        sprite.rect.x, sprite.rect.y = (
            pygame.Vector2(
                sprite.col * self.tile_width,
                sprite.row * self.tile_height,
            )
            + self.offset
        )

    def is_wall(self, col, row):
        return self.tile_at_layer(col, row, self.primary_collision_layer_id) is not None

    def reset(self):
        self.empty()
        self.player = None
        self.ghost = None
        for entity in self.entity_loader_func():
            entity.world = self
            if isinstance(entity, Player):
                self.player = entity
            # if isinstance(entity, Ghost):
            #     self.ghost = entity
            self.add(entity)
            entity.post_init()

    def render(self, screen):
        """
        A rendering method that calls both the map rendering and sprite rendering method
        """
        # clear the entire surface
        self.surface.fill((0, 0, 0, 0))

        # render the map layer
        self.pyscroll_group.draw(self.surface)

        # render the sprites
        self.update()

        return screen.blit(self.surface, self.offset)

    def event(self, event):
        if self.gameover:
            return
        for sprite in self.sprites():
            if isinstance(sprite, TileAlignedEntity):
                sprite.event(event)


def load():
    pbb = [
        Player(
            images.sprites.player_stick,
            (3, 3),
            smooth_move_animation=True,
            images=images.sprites,
            z=1,
        ),
        Box(
            images.sprites.test_tile,
            (5, 4),
            smooth_move_animation=True,
        ),
        Box(
            images.sprites.number_tile[1],
            (5, 6),
            smooth_move_animation=True,
        ),
    ]

    door = Door(images.sprites.door_open, (7, 4), images=images.sprites)

    def on_update(value):
        door.open = value

    box2 = Switch(
        images.sprites.switch_on,
        (7, 6),
        on_update=on_update,
        images=images.sprites,
    )
    return [*pbb, door, box2]


world = World(
    "resources/maps/animation-test.tmx", (1000, 1000), entity_loader_func=load, moves=30
)

# # Load TMX data
# tmx_data = load_pygame("resources/maps/animation-test.tmx")

# # Make the scrolling layer
# map_layer = pyscroll.BufferedRenderer(
#     pyscroll.TiledMapData(tmx_data),
#     (400, 400),
#     alpha=True,
# )

# # make the pygame SpriteGroup with a scrolling map
# group = pyscroll.PyscrollGroup(map_layer)

# # Add sprite(s) to the group
# image = pygame.image.load("resources/images/sprites/test-tile.png").convert_alpha()
# camera = Sprite(image)
# group.add(camera)

# # Center the camera on the sprite
# group.center(camera.rect.center)

# # Draw map and sprites using the group
# # Notice I did not `screen.fill` here!  Clearing the screen is not
# # needed since the map will clear it when drawn

# bb = False

# x = y = 0

# map_layer.reload()

# map_layer.zoom -= 0.01

while running:

    dx = dy = 0
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                world.reset()
        world.event(e)

    # if pygame.key.get_pressed()[pygame.K_d]:
    #     x += 10
    # if pygame.key.get_pressed()[pygame.K_s]:
    #     y += 10
    # if pygame.key.get_pressed()[pygame.K_a]:
    #     x -= 10
    # if pygame.key.get_pressed()[pygame.K_w]:
    #     y -= 10

    # # game logic
    # camera.rect.x = x
    # camera.rect.y = y
    # group.center((x, y))
    # group.update()
    screen.fill(pygame.Color("white"))

    # print(player.row, player.col, player.rect)

    # world.offset = (int(random.random() * 30), int(random.random() * 30))

    world.render(screen)

    # screen.fill(pygame.Color("black"))

    # if bb:
    #     for i in sprites:
    #         pygame.draw.rect(screen, i.color, i.rect)
    # else:
    #     for i in sprites:
    #         i.update()

    # group.draw(screen)

    # screen.blit(player.image, (100, 100))

    pygame.display.update()

    clock.tick(60)
