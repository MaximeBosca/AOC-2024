import re

from aoc2024.commons import load_data

DAY_NUMBER = '03'

REGEXP = "(mul\\(\\d{1,3},\\d{1,3}\\))|(do\\(\\))|(don't\\(\\))"


def solve_part_one(data: str) -> int:
    return 0


def solve_part_two(data: str) -> int:
    total = 0
    do = True
    commands = re.findall(REGEXP, data)
    for mul_command, do_command, dont_command in commands:
        if do_command:
            do = True
            continue
        if dont_command:
            do = False
            continue
        if do:
            total += process_command(mul_command)
    return total


def process_command(command: str) -> int:
    left_number, right_number = command[4:-1].split(',')
    return int(left_number) * int(right_number)


def main():
    data = load_data(DAY_NUMBER)
    print('Part one solved :', solve_part_one(data))
    print('Part two solved :', solve_part_two(data))


if __name__ == '__main__':
    main()
