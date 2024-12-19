import aoc2024.day_12 as d12
from aoc2024.commons import load_data

DAY_NUMBER = '12'
TEST_PREFIX = 'test_'
BABY_TEST_PREFIX = 'baby_test_'
MEDIUM_TEST_PREFIX = 'medium_test_'
EXPECTED_PART_ONE = 1930
EXPECTED_PART_TWO = 1206
BABY_EXPECTED_PART_ONE = 140
MEDIUM_EXPECTED_PART_ONE = 772


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d12.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_baby_part_one():
    test_input = load_data(DAY_NUMBER, prefix=BABY_TEST_PREFIX)
    assert (d12.solve_part_one(test_input)) == BABY_EXPECTED_PART_ONE


def test_medium_part_one():
    test_input = load_data(DAY_NUMBER, prefix=MEDIUM_TEST_PREFIX)
    assert (d12.solve_part_one(test_input)) == MEDIUM_EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d12.solve_part_two(test_input)) == EXPECTED_PART_TWO
