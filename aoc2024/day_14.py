import numpy

from aoc2024.commons import load_data, time_function, beautify_time_ns
from aoc2024.coordinates import Coord
import re

DAY_NUMBER = '14'


class Robot:
    def __init__(self, start: Coord, velocity: Coord):
        self.start = start
        self.velocity = velocity


def compute_position(robot: Robot, bounds: Coord, time: int):
    new_x = (robot.start[0] + robot.velocity[0] * time) % bounds[0]
    new_y = (robot.start[1] + robot.velocity[1] * time) % bounds[1]
    return Coord(new_x, new_y)


def get_quadrant(final_position, bounds):
    is_left = final_position[0] < bounds[0] // 2
    is_right = final_position[0] >= (bounds[0] + 1) // 2
    is_up = final_position[1] < bounds[1] // 2
    is_down = final_position[1] >= (bounds[1] + 1) // 2
    if is_left and is_up:
        return 1, 0, 0, 0
    if is_left and is_down:
        return 0, 1, 0, 0
    if is_right and is_up:
        return 0, 0, 1, 0
    if is_right and is_down:
        return 0, 0, 0, 1
    return 0, 0, 0, 0


def solve_part_one(data: str, bounds: Coord = Coord(101, 103)) -> int:
    robots = load_robots(data)
    quadrants = (0, 0, 0, 0)
    for robot in robots:
        final_position = compute_position(robot, bounds, 100)
        new_quadrant = get_quadrant(final_position, bounds)
        quadrants = tuple([new + quadrants[i] for i, new in enumerate(new_quadrant)])
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def print_map(positions: list[Coord], bounds):
    result = numpy.zeros([bounds[1], bounds[0]])
    for position in positions:
        result[position[1]][position[0]] += 1
    print('Map is :')
    print(result)


def solve_part_two(data: str, bounds: Coord = Coord(101, 103)) -> int:
    robots = load_robots(data)
    positions = []
    for time in range(0, 100):
        for robot in robots:
            positions.append(compute_position(robot, bounds, time))
        print_map(positions, bounds)
    return 0


def load_robot(line: str):
    x, y, vx, vy = [int(value) for value in re.match(r'p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)', line).groups()]
    return Robot(start=Coord(x, y), velocity=Coord(vx, vy))


def load_robots(data: str) -> list[Robot]:
    lines = data.strip().split('\n')
    robots = []
    for line in lines:
        robots.append(load_robot(line))
    return robots


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
