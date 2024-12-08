from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '04'

NORTH = (1, 0)
SOUTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)
N_E = (1, 1)
N_W = (1, -1)
S_E = (-1, 1)
S_W = (-1, -1)
DIRECTIONS = [NORTH, SOUTH, EAST, WEST, N_E, N_W, S_E, S_W]
X_MAS = 'XMAS'


def solve_part_one(data: str) -> int:
    xmas_number = 0
    lines = data.strip().split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == X_MAS[0]:
                for direction in DIRECTIONS:
                    xmas_number += 1 if find_string(lines, x, y, direction, X_MAS) else 0
    return xmas_number


def find_cross(data: list[str], x: int, y: int) -> bool:
    if x < 1 or y < 1 or x >= len(data[0]) - 1 or y >= len(data) - 1:
        return False
    [nw, sw, ne, se] = [data[y + direction[0]][x + direction[1]] for direction in (N_W, S_W, N_E, S_E)]
    cross_1 = (nw == 'M' and se == 'S') or (nw == 'S' and se == 'M')
    cross_2 = (ne == 'M' and sw == 'S') or (ne == 'S' and sw == 'M')
    return cross_1 and cross_2


def solve_part_two(data: str) -> int:
    xmas_number = 0
    lines = data.strip().split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'A':
                xmas_number += 1 if find_cross(lines, x, y) else 0
    return xmas_number


def find_string(data: list[str], x_start: int, y_start: int, direction: tuple[int, int], string: str) -> bool:
    for i, char in enumerate(string):
        x = x_start + direction[1] * i
        y = y_start + direction[0] * i
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return False
        if data[y][x] != char:
            return False
    return True


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
