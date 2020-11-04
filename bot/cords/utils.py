from math import sqrt
from bot.cords.point import Point


SQRT_2 = sqrt(2)


def diagonal(width: int):
    return int(width * SQRT_2)


def adjacent_tiles(center: Point, tile_width: int):
    diag = diagonal(tile_width)
    return [
        center.shift(tile_width, 0),  # right
        center.shift(-tile_width, 0),
        center.shift(0, tile_width),
        center.shift(0, -tile_width),
        center.shift(diag, diag),
        center.shift(-diag, diag),
        center.shift(-diag, -diag),
        center.shift(diag, -diag),
    ]
