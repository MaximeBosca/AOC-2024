import aoc2024.day_15 as d15
from aoc2024.commons import load_data

DAY_NUMBER = '15'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 0
EXPECTED_PART_TWO = 0


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d15.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d15.solve_part_two(test_input)) == EXPECTED_PART_TWO
