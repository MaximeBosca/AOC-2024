import aoc2024.day_06 as d06
from aoc2024.commons import load_data

DAY_NUMBER = '06'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 41
EXPECTED_PART_TWO = 6


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d06.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d06.solve_part_two(test_input)) == EXPECTED_PART_TWO
