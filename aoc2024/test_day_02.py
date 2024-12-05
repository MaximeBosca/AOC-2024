import pytest

from day_02 import is_report_safe


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3, 4, 5], True),
    ([1, 2, 3, 3, 3, 4], False),
    ([1, 2, 3, 6, 4, 5], True),
    ([1, 2, 3, 6, 12], True),
    ([1, 2, 3, 6, 4, 8], True),
    ([1, 2, 3, 6, 4, 8, 9], True),
    ([1, 2, 3, 6, 2], True),
    ([4, 5, 4, 3, 2, 1], True),
    ([5, 4, 7, 8, 9, 10], True),
    ([5, 4, 7, 8, 9, 10, 11, 11], False),
    ([5, 4, 7, 8, 9, 10, 11, 11, 12], False),
    ([1, 2, 3, 2], True),
    ([4, 2, 1, 4, 6, 5], False),
])
def test_is_report_safe(test_input, expected: bool):
    assert is_report_safe(test_input) == expected


def test_is_safe():
    assert is_report_safe([4, 5, 4, 3, 2, 1]) is True
