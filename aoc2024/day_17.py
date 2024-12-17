from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '17'


def solve_part_one(data: str) -> int:
    return 0


def solve_part_two(data: str) -> int:
    return 0


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
