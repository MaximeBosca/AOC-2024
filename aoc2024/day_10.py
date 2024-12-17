from aoc2024.commons import load_data, time_function, beautify_time_ns
from aoc2024.coordinates import Coord, get_bounds, is_in_bounds, Direction

DAY_NUMBER = '10'


def get_accessible_nines(coord: Coord, current: int, bounds: Coord, lines: list[str]) -> set[Coord]:
    if current == 9:
        return {coord}
    accessible_nines = set()
    for direction in Direction:
        new_coord = Coord(coord.row + direction.row, coord.col + direction.col)
        if is_in_bounds(new_coord, bounds=bounds):
            new = int(lines[new_coord.row][new_coord.col])
            if new == current + 1:
                accessible_nines.update(get_accessible_nines(new_coord, new, bounds, lines))
    return accessible_nines


def get_rating(coord: Coord, current: int, bounds: Coord, lines: list[str]) -> int:
    if current == 9:
        return 1
    rating = 0
    for direction in Direction:
        new_coord = Coord(coord.row + direction.row, coord.col + direction.col)
        if is_in_bounds(new_coord, bounds=bounds):
            new = int(lines[new_coord.row][new_coord.col])
            if new == current + 1:
                rating += get_rating(new_coord, new, bounds, lines)
    return rating


def solve_part_one(data: str) -> int:
    trail_score = 0
    lines = data.strip().split('\n')
    bounds = get_bounds(data)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '0':
                trail_score += len(get_accessible_nines(Coord(row, col),
                                                        current=int(char),
                                                        bounds=bounds,
                                                        lines=lines))
    return trail_score


def solve_part_two(data: str) -> int:
    rating = 0
    lines = data.strip().split('\n')
    bounds = get_bounds(data)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '0':
                rating += get_rating(Coord(row, col),
                                     current=int(char),
                                     bounds=bounds,
                                     lines=lines)
    return rating


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
