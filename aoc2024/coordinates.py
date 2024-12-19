from collections import namedtuple
from enum import Enum

Coord = namedtuple('Coord', ['row', 'col'])


def get_bounds(data: str) -> Coord:
    lines = data.strip().split('\n')
    return Coord(len(lines), len(lines[0]))


def is_in_bounds(coord: Coord, bounds: Coord) -> bool:
    return 0 <= coord[0] < bounds[0] and 0 <= coord[1] < bounds[1]


def is_before(first: Coord, second: Coord) -> bool:
    if first.row < second.row:
        return True
    if first.col < second.col:
        return True
    if first.col == second.col and first.row == second.row:
        return True
    return False


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, row, col):
        self.row = row
        self.col = col
