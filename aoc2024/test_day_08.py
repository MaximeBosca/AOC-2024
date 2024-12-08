import aoc2024.day_08 as d08
from aoc2024.commons import load_data

DAY_NUMBER = '08'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 14
EXPECTED_PART_TWO = 34


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d08.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d08.solve_part_two(test_input)) == EXPECTED_PART_TWO
