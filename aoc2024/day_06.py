from enum import Enum, auto

from aoc2024.commons import load_data

DAY_NUMBER = '06'


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def turn_right(self):
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP


class Map:
    def __init__(self, col_boundary: int, row_boundary: int):
        self.col_obstacles: dict[int, list[int]] = dict()
        self.row_obstacles: dict[int, list[int]] = dict()
        self.col_boundary = col_boundary
        self.row_boundary = row_boundary

    def add_obstacle(self, row: int, col: int) -> None:
        self.col_obstacles.setdefault(col, []).append(row)
        self.row_obstacles.setdefault(row, []).append(col)

    def get_obstacle(self, row: int, col: int, direction: Direction) -> int:
        match direction:
            case Direction.UP:
                obstacle_list = self.col_obstacles.get(col, [])
                return max(filter(lambda obs_pos: obs_pos < row, obstacle_list), default=-1)
            case Direction.DOWN:
                obstacle_list = self.col_obstacles.get(col, [])
                return min(filter(lambda obs_pos: obs_pos > row, obstacle_list), default=-1)
            case Direction.LEFT:
                obstacle_list = self.row_obstacles.get(row, [])
                return max(filter(lambda obs_pos: obs_pos < col, obstacle_list), default=-1)
            case Direction.RIGHT:
                obstacle_list = self.row_obstacles.get(row, [])
                return min(filter(lambda obs_pos: obs_pos > col, obstacle_list), default=-1)

    def copy(self):
        new = Map(col_boundary=self.col_boundary, row_boundary=self.row_boundary)
        new.row_obstacles = dict()
        for row, obstacles in self.row_obstacles.items():
            new.row_obstacles[row] = obstacles.copy()
        new.col_obstacles = dict()
        for col, obstacles in self.col_obstacles.items():
            new.col_obstacles[col] = obstacles.copy()
        return new


class PathPoint:
    def __init__(self, row: int, col: int, direction: Direction):
        self.row = row
        self.col = col
        self.direction = direction

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, PathPoint):
            return False
        return self.row == o.row and self.col == o.col and self.direction == o.direction

    def __hash__(self) -> int:
        return hash(str(self.row) + str(self.col) + str(self.direction))

    def __repr__(self):
        return str(self.row) + ' ' + str(self.col) + ' ' + str(self.direction)


class Guard:
    def __init__(self, row: int, col: int, map: Map):
        self.row, self.col = row, col
        self.direction = Direction.UP
        self.map = map
        self.path: set[PathPoint] = set()
        self.is_free, self.is_loop = False, False

    def move(self):
        if PathPoint(row=self.row, col=self.col, direction=self.direction) in self.path:
            self.is_loop = True
            return
        obs_pos = self.map.get_obstacle(row=self.row, col=self.col, direction=self.direction)
        if obs_pos == -1:
            self.is_free = True
            self.add_final_path()
            return
        match self.direction:
            case Direction.UP:
                new_row = obs_pos + 1
                self.path.update([PathPoint(row=row, col=self.col, direction=self.direction)
                                  for row in range(new_row + 1, self.row + 1)])
                self.row = new_row
            case Direction.DOWN:
                new_row = obs_pos - 1
                self.path.update([PathPoint(row=row, col=self.col, direction=self.direction)
                                  for row in range(self.row, new_row)])
                self.row = new_row
            case Direction.LEFT:
                new_col = obs_pos + 1
                self.path.update([PathPoint(row=self.row, col=col, direction=self.direction)
                                  for col in range(new_col + 1, self.col + 1)])
                self.col = new_col
            case Direction.RIGHT:
                new_col = obs_pos - 1
                self.path.update([PathPoint(row=self.row, col=col, direction=self.direction)
                                  for col in range(self.col, new_col)])
                self.col = new_col
        self.direction = self.direction.turn_right()

    def add_final_path(self):
        match self.direction:
            case Direction.UP:
                self.path.update([PathPoint(row=row, col=self.col, direction=self.direction)
                                  for row in range(0, self.row + 1)])
            case Direction.DOWN:
                self.path.update([PathPoint(row=row, col=self.col, direction=self.direction)
                                  for row in range(self.row, self.map.row_boundary)])
            case Direction.LEFT:
                self.path.update([PathPoint(row=self.row, col=col, direction=self.direction)
                                  for col in range(0, self.col + 1)])
            case Direction.RIGHT:
                self.path.update([PathPoint(row=self.row, col=col, direction=self.direction)
                                  for col in range(self.col, self.map.col_boundary)])

    def reset(self, starting_col: int, starting_row: int, starting_direction: Direction):
        self.is_free, self.is_loop = False, False
        self.col = starting_col
        self.row = starting_row
        self.direction = starting_direction
        self.path = set()


def solve_part_one(data: str) -> int:
    guard, initial_map = parse_map(data)
    while not guard.is_free:
        guard.move()
    return len(set(map(lambda pathpoint: (pathpoint.row, pathpoint.col), guard.path)))


def solve_part_two(data: str) -> int:
    guard, initial_map = parse_map(data)
    starting_col, starting_row, starting_direction = guard.col, guard.row, guard.direction
    while not guard.is_free:
        guard.move()
    initial_path = set(map(lambda pathpoint: (pathpoint.row, pathpoint.col), guard.path))
    valid_obstructions = 0
    i = 0
    for row, col in initial_path:
        i += 1
        if row == starting_row and col == starting_col:
            continue
        new_map = initial_map.copy()
        new_map.add_obstacle(row, col)
        guard.reset(starting_col=starting_col, starting_row=starting_row, starting_direction=starting_direction)
        guard.map = new_map
        if is_valid_obstruction(guard):
            valid_obstructions += 1
            print("({row}, {col})".format(row=row, col=col))
    return valid_obstructions


def is_valid_obstruction(guard: Guard) -> bool:
    while not (guard.is_free or guard.is_loop):
        guard.move()
    return guard.is_loop


def parse_map(data: str) -> tuple[Guard, Map]:
    grid = data.strip().split('\n')
    row_boundary = len(grid)
    col_boundary = len(grid[0])
    initial_map = Map(row_boundary=row_boundary, col_boundary=col_boundary)
    guard = None
    for row, line in enumerate(grid):
        for col, character in enumerate(line):
            if character == '^':
                guard = Guard(row=row, col=col, map=initial_map)
                continue
            if character == '#':
                initial_map.add_obstacle(row=row, col=col)
    return guard, initial_map


def main():
    data = load_data(DAY_NUMBER)
    print('Part one solved :', solve_part_one(data))
    print('Part two solved :', solve_part_two(data))


if __name__ == '__main__':
    main()
