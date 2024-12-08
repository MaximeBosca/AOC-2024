from typing import Callable

from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '07'

Binary = Callable[[int, int], int]


def mult(x: int, y: int) -> int:
    return x * y


def add(x: int, y: int) -> int:
    return x + y


def concat(x: int, y: int) -> int:
    return int(str(x) + str(y))


OPERATORS_PART_ONE: list[Binary] = [mult, add]
OPERATORS_PART_TWO: list[Binary] = [mult, add, concat]


def is_valid(expected: int, numbers: list[int], operators: list[Binary]) -> bool:
    results = [numbers[0]]
    remaining = numbers[1:]
    for current in remaining:
        current_result = []
        for operator in operators:
            current_result.extend([operator(res, current) for res in results])
        results = list(filter(lambda res: res <= expected, current_result))
    if expected in results:
        return True
    return False


def solve_part_one(data: str) -> int:
    lines = data.strip().split('\n')
    result = 0
    for line in lines:
        expected_str, numbers_str = line.strip().split(':')
        expected = int(expected_str)
        numbers = [int(nb) for nb in numbers_str.strip().split(' ')]
        result += expected if is_valid(expected, numbers, OPERATORS_PART_ONE) else 0
    return result


def solve_part_two(data: str) -> int:
    lines = data.strip().split('\n')
    result = 0
    for line in lines:
        expected_str, numbers_str = line.strip().split(':')
        expected = int(expected_str)
        numbers = [int(nb) for nb in numbers_str.strip().split(' ')]
        result += expected if is_valid(expected, numbers, OPERATORS_PART_TWO) else 0
    return result


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
