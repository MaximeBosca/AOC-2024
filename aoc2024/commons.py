from pathlib import Path
from time import perf_counter_ns
from typing import Callable, TypeVar

T = TypeVar('T')
TIME_UNITS = [('µs', 1000), ('ms', 1000), ('s', 1000), ('m', 60), ('h', 60)]


def load_data(day_number: str, prefix: str = '') -> str:
    pathname = Path(__file__).parent.parent / 'data' / f"{prefix}input_{day_number:02}.txt"
    return pathname.read_text()


def time_function(function: Callable[..., T], *args, **kwargs) -> tuple[T, int]:
    start_time = perf_counter_ns()
    result = function(*args, **kwargs)
    return result, perf_counter_ns() - start_time


def beautify_time_ns(time_ns: int) -> str:
    time = time_ns
    unit = 'ns'
    remainder = None
    previous_unit = None
    for new_unit, factor in TIME_UNITS:
        new_time = time // factor
        if new_time == 0:
            break
        remainder = time % factor
        previous_unit = unit
        unit = new_unit
        time = new_time
    if not remainder:
        return '{time}{unit}'.format(time=time, unit=unit)
    return '{time}{unit} {remainder}{previous_unit}' \
        .format(time=time, unit=unit, remainder=remainder, previous_unit=previous_unit)
