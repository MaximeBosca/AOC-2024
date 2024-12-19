from aoc2024.commons import load_data, time_function, beautify_time_ns
import numpy as np
import re

DAY_NUMBER = '13'


class Machine:
    def __init__(self, button_a, button_b, prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize


def determinant(matrix: np.matrix) -> int:
    return matrix[0, 0] * matrix[1, 1] - matrix[1, 0] * matrix[0, 1]


def solve(machine: Machine):
    a = machine.button_a[0]
    b = machine.button_b[0]
    c = machine.button_a[1]
    d = machine.button_b[1]
    e = machine.prize[0]
    f = machine.prize[1]
    det = a*d - b*c
    if det == 0:
        return 0
    if (e * d - b * f) % det != 0 or (a * f - e * c) % det != 0:
        return 0
    x = (e * d - b * f) // det
    y = (a * f - e * c) // det
    if x < 0 or y < 0:
        return 0
    return 3 * x + y


def solve_part_one(data: str) -> int:
    machines = load_machines(data)
    tokens = 0
    for machine in machines:
        tokens += solve(machine)
    return tokens


def solve_part_two(data: str) -> int:
    machines = load_machines(data)
    tokens = 0
    for machine in machines:
        machine.prize = (machine.prize[0] + 10000000000000, machine.prize[1] + 10000000000000)
        tokens += solve(machine)
    return tokens


def load_button(line):
    n1, n2 = re.match(r'Button .: X\+(\d*), Y\+(\d*)', line).groups()
    return int(n1), int(n2)


def load_prize(line):
    n1, n2 = re.match(r'Prize: X=(\d*), Y=(\d*)', line).groups()
    return int(n1), int(n2)


def load_machines(data: str) -> list[Machine]:
    lines = data.strip().split('\n')
    machines = []
    button_a, button_b, prize = None, None, None
    for line in lines:
        if line.startswith('Button A'):
            button_a = load_button(line)
        if line.startswith('Button B'):
            button_b = load_button(line)
        if line.startswith('Prize'):
            prize = load_prize(line)
            machines.append(Machine(button_a=button_a, button_b=button_b, prize=prize))
    return machines


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
