from aoc2024.commons import load_data, time_function, beautify_time_ns
from aoc2024.coordinates import Coord, get_bounds, is_in_bounds, Direction, is_before

DAY_NUMBER = '12'

CORNERS = [(Direction.UP, Direction.LEFT),
           (Direction.UP, Direction.RIGHT),
           (Direction.DOWN, Direction.LEFT),
           (Direction.DOWN, Direction.RIGHT)]


class Plot:
    def __init__(self, letter: chr, area: int, perimeter: int, sides: int, positions: set[Coord]):
        self.letter = letter
        self.positions = positions
        self.area = area
        self.perimeter = perimeter
        self.sides = sides

    def __repr__(self):
        return ("letter : {letter}, area : {area}, perimeter : {perimeter}, sides : {sides}"
                .format(letter=self.letter, area=self.area, perimeter=self.perimeter, sides=self.sides))


def get_2d_map(data: str) -> list[str]:
    return data.strip().split('\n')


def merge_plots(first: Plot, second: Plot, plots: dict[Coord, Plot]) -> Plot:
    if first == second:
        return first
    for pos in second.positions:
        plots[pos] = first
        first.positions.add(pos)
    first.area += second.area
    first.perimeter += second.perimeter
    first.sides += second.sides
    return first


def solve_part_one(data: str) -> int:
    plots = get_plots(data)
    return sum(map(lambda p: p.perimeter * p.area, plots))


def is_different(direction: Direction, pos: Coord, letter: chr, field: list[str], bounds: Coord) -> bool:
    new_pos = Coord(row=pos.row + direction.row, col=pos.col + direction.col)
    if not is_in_bounds(new_pos, bounds):
        return True
    other = field[new_pos.row][new_pos.col]
    if other != letter:
        return True
    return False


def is_same(direction: Direction, pos: Coord, letter: chr, field: list[str], bounds: Coord):
    return not is_different(direction ,pos, letter, field, bounds)


def is_corner(corner: tuple[Direction, Direction], pos: Coord, letter: chr, field: list[str], bounds: Coord) -> bool:
    if is_different(corner[0], pos, letter, field, bounds) and is_different(corner[1], pos, letter, field, bounds):
        return True
    pos_1 = Coord(row=pos.row + corner[1].row, col=pos.col + corner[1].col)
    if (is_same(corner[0], pos, letter, field, bounds)
            and is_same(corner[1], pos, letter, field, bounds)
            and is_different(corner[0], pos_1, letter, field, bounds)):
        return True
    return False


def get_plots(data):
    bounds = get_bounds(data)
    plots: dict[Coord, Plot] = dict()
    field = get_2d_map(data)
    for row, line in enumerate(field):
        for col, char in enumerate(line):
            pos = Coord(row=row, col=col)
            area = 1
            perimeter = 0
            plot = None
            sides = 0
            for direction in Direction:
                new_pos = Coord(row=row + direction.row, col=col + direction.col)
                if not is_in_bounds(new_pos, bounds):
                    perimeter += 1
                    continue
                other = field[new_pos.row][new_pos.col]
                if other != char:
                    perimeter += 1
                    continue
                if is_before(new_pos, pos):
                    if plot:
                        plot = merge_plots(plot, plots[new_pos], plots)
                    else:
                        plot = plots[new_pos]
            for corner in CORNERS:
                sides += 1 if is_corner(corner, pos, char, field, bounds) else 0
            if not plot:
                plot = Plot(char, 0, 0, 0, {pos})
            plot.area += area
            plot.perimeter += perimeter
            plot.sides += sides
            plot.positions.add(pos)
            plots[pos] = plot
    return set(plots.values())


def solve_part_two(data: str) -> int:
    plots = get_plots(data)
    return sum(map(lambda p: p.sides * p.area, plots))


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
