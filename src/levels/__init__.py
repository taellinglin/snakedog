from engine.world import *


class Level:
    def __init__(self, entities=None, particles=None):
        self.entities = entities or []
        self.particles = particles or []


def level_1():

    pbb = [
        ExitDoor(images.sprites.exit, (3, 2)),
        Player(
            images.sprites.player_stick,
            (3, 3),
            smooth_move_animation=True,
            images=images.sprites,
            z=1,
        ),
        Box(
            images.sprites.test_tile,
            (4, 4),
            smooth_move_animation=True,
        ),
        Box(
            images.sprites.number_tile[1],
            (5, 6),
            smooth_move_animation=True,
        ),
        TimePiece(images.sprites.timepiece, (5, 8)),
    ]

    door = Door(
        images.sprites.door_open,
        (7, 4),
        images=images.sprites,
        smooth_move_animation=True,
    )

    def on_update(value):
        door.open = value

    box2 = Switch(
        images.sprites.switch_on,
        (7, 6),
        on_update=on_update,
        images=images.sprites,
    )

    return Level([*pbb, door, box2], [])


levels = [None, level_1]
