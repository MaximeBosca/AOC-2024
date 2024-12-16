import pytest

import aoc2024.day_09 as d09
from aoc2024.commons import load_data

DAY_NUMBER = '09'
TEST_PREFIX = 'test_'
EXPECTED_PART_ONE = 1928
EXPECTED_PART_TWO = 2858


def test_part_one():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d09.solve_part_one(test_input)) == EXPECTED_PART_ONE


def test_part_two():
    test_input = load_data(DAY_NUMBER, prefix=TEST_PREFIX)
    assert (d09.solve_part_two(test_input)) == EXPECTED_PART_TWO


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 6, 11),
    (1, 10, 55),
    (23, 30, 212),
    (5, 5, 5)
])
def test_sum_a_to_b(a, b, expected):
    assert d09.sum_a_to_b(a, b) == expected


@pytest.mark.parametrize("size, expected", [
    (2, 0),
    (3, 2),
    (4, 2),
    (6, 4),
    (7, 6),
    (8, 6),
    (10, 8),
    (11, 10)
])
def test_get_end_file_index(size, expected):
    assert d09.get_end_file_index(size) == expected


@pytest.mark.parametrize("size, expected", [
    (2, 0),
    (3, 1),
    (4, 1),
    (6, 2),
    (7, 3),
    (8, 3),
    (10, 4),
    (11, 5)
])
def test_get_end_file_number(size, expected):
    assert d09.get_end_file_number(size) == expected
