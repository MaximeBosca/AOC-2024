import pytest

from aoc2024.commons import beautify_time_ns


@pytest.mark.parametrize("test_input, expected", [
    (300, '300ns'),
    (3000, '3µs'),
    (3000000, '3ms'),
    (3000000000, '3s'),
    (60000000000, '1m'),
    (3600000000000, '1h'),
    (3500, '3µs 500ns'),
    (3050000, '3ms 50µs'),
    (3100000000, '3s 100ms'),
    (125000000000, '2m 5s'),
    (3660000000000, '1h 1m'),
    (3050040, '3ms 50µs'),
])
def test_beautify_time_ns(test_input, expected):
    assert beautify_time_ns(test_input) == expected
