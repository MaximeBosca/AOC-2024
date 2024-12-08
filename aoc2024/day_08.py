from itertools import combinations

from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '08'

Coord = tuple[int, int]


def get_antennas(data: str) -> dict[str, list[Coord]]:
    antennas: dict[str, list[Coord]] = dict()
    lines = data.strip().split('\n')
    for row, line in enumerate(lines):
        for col, character in enumerate(line):
            if character != '.':
                antennas.setdefault(character, []).append((row, col))
    return antennas


def get_bounds(data: str) -> Coord:
    lines = data.strip().split('\n')
    return len(lines), len(lines[0])


def is_in_bounds(coord: Coord, bounds: Coord) -> bool:
    return 0 <= coord[0] < bounds[0] and 0 <= coord[1] < bounds[1]


def get_antinode_pair(combination: tuple[Coord, Coord], bounds: Coord) -> list[Coord]:
    (row1, col1), (row2, col2) = combination
    return list(filter(lambda coord: is_in_bounds(coord, bounds),
                       [(2 * row1 - row2, 2 * col1 - col2), (2 * row2 - row1, 2 * col2 - col1)]))


def get_antinode_list(combination: tuple[Coord, Coord], bounds: Coord) -> set[Coord]:
    (row1, col1), (row2, col2) = combination
    antinodes = set()
    i = 0
    in_bounds_one = True
    in_bounds_two = True
    while in_bounds_one or in_bounds_two:
        new_coord_one = (row1 - i * (row2 - row1), col1 - i * (col2 - col1))
        new_coord_two = (row2 - i * (row1 - row2), col2 - i * (col1 - col2))
        if not is_in_bounds(new_coord_one, bounds):
            in_bounds_one = False
        if not is_in_bounds(new_coord_two, bounds):
            in_bounds_two = False
        if in_bounds_one:
            antinodes.add(new_coord_one)
        if in_bounds_two:
            antinodes.add(new_coord_two)
        i += 1
    return antinodes


def get_antinodes(positions: list[Coord], bounds: Coord) -> set[Coord]:
    antinodes: set[Coord] = set()
    for combination in list(combinations(positions, 2)):
        antinodes.update(get_antinode_pair(combination=combination, bounds=bounds))
    return antinodes


def get_antinodes_part_two(positions: list[Coord], bounds: Coord) -> set[Coord]:
    antinodes: set[Coord] = set()
    for combination in list(combinations(positions, 2)):
        antinodes.update(get_antinode_list(combination=combination, bounds=bounds))
    return antinodes


def solve_part_one(data: str) -> int:
    antennas = get_antennas(data)
    bounds = get_bounds(data)
    antinodes: set[Coord] = set()
    for positions in antennas.values():
        antinodes.update(get_antinodes(positions=positions, bounds=bounds))
    return len(antinodes)


def solve_part_two(data: str) -> int:
    antennas = get_antennas(data)
    bounds = get_bounds(data)
    antinodes: set[Coord] = set()
    for positions in antennas.values():
        antinodes.update(get_antinodes_part_two(positions=positions, bounds=bounds))
    return len(antinodes)


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
