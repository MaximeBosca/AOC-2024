import aoc2024.day_14 as d14
from aoc2024.commons import load_data
from aoc2024.coordinates import Coord

DAY_NUMBER = '14'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 12
EXPECTED_PART_TWO = 0


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d14.solve_part_one(test_input, bounds=Coord(11, 7))) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d14.solve_part_two(test_input, bounds=Coord(11, 7))) == EXPECTED_PART_TWO
