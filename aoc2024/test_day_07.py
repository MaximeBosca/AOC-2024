import pytest

import aoc2024.day_07 as d07
from aoc2024.commons import load_data

DAY_NUMBER = '07'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 3749
EXPECTED_PART_TWO = 11387


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d07.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d07.solve_part_two(test_input)) == EXPECTED_PART_TWO


@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 12),
    (12, 2, 122),
    (4, 6, 46)
])
def test_concat(x, y, expected):
    assert d07.concat(x, y) == expected
