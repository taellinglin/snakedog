import pygame


def pygame_event_to_dxdy(e):
    """
    Returns None if the key pressed is not relevant
    """
    if e.type != pygame.KEYDOWN:
        return
    return {
        pygame.K_w: (0, -1),
        pygame.UP: (0, -1),
        pygame.K_a: (-1, 0),
        pygame.LEFT: (-1, 0),
        pygame.K_s: (0, 1),
        pygame.DOWN: (0, 1),
        pygame.K_d: (1, 0),
        pygame.RIGHT: (1, 0),
    }.get(e.key, None)


def is_restart(e):
    """
    Returns True if the key is restart
    """
    return e.type == pygame.KEYDOWN and e.key == pygame.K_r
