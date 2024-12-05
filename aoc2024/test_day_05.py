import pytest

import aoc2024.day_05 as d05
from aoc2024.commons import load_data

DAY_NUMBER = '05'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 143
EXPECTED_PART_TWO = 123


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d05.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d05.solve_part_two(test_input)) == EXPECTED_PART_TWO


@pytest.mark.parametrize("test_input, expected", [
    ([75, 47, 61, 53, 29], 61),
    ([97, 61, 53, 29, 13], 53),
    ([75, 29, 13], 29),
    ([75, 97, 47, 61, 53], 47),
    ([61, 13, 29], 13),
    ([97, 13, 75, 29, 47], 75)
])
def test_get_middle_page(test_input, expected):
    assert d05.get_middle_page(test_input) == expected
