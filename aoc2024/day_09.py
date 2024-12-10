from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '09'


class Remaining:
    def __init__(self, remaining_space: int = 0, remaining_file: int = 0):
        self.remaining_space = remaining_space
        self.remaining_file = remaining_file


def get_end_file_index(total_size: int):
    return total_size - 2 if total_size % 2 == 0 else total_size - 1


def get_end_file_number(total_size: int):
    return (total_size - 1) // 2


def fill_empty_spot(remaining: Remaining, file_number: int, start_index: int) -> tuple[int, int]:
    effective_size = min(remaining.remaining_space, remaining.remaining_file)
    remaining.remaining_space = remaining.remaining_space - effective_size
    remaining.remaining_file = remaining.remaining_file - effective_size
    checksum = get_checksum(file_number, start_index, start_index + effective_size)
    return checksum, effective_size


def solve_part_one(data: str) -> int:
    print('Starting to solve')
    checksum = 0
    file_number = 0
    index = 0
    is_file = True
    total_size = len(data)
    end_data_index = get_end_file_index(total_size)
    end_file_number = get_end_file_number(total_size)
    end_file_size = int(data[end_data_index])
    remaining = Remaining(0, end_file_size)
    for char in data:
        size = int(char)
        if is_file:
            checksum += get_checksum(file_number=file_number, start_index=index, end_index=index + size)
            file_number += 1
        else:
            remaining.remaining_space += size
            fill_start_index = index
            while remaining.remaining_space != 0:
                checksum_to_add, filled_size = fill_empty_spot(remaining, end_file_number, fill_start_index)
                fill_start_index += filled_size
                checksum += checksum_to_add
                if not remaining.remaining_file:
                    end_file_number -= 1
                    end_data_index -= 2
                    remaining.remaining_file = int(data[end_data_index])
        index += size
        is_file = not is_file
        if file_number >= end_file_number:
            break
    if remaining.remaining_file:
        checksum += get_checksum(end_file_number, index, index+remaining.remaining_file)
    return checksum


def get_checksum(file_number: int, start_index: int, end_index: int) -> int:
    return 0 if file_number == 0 or end_index < start_index + 1 \
        else file_number * sum_a_to_b(start_index, end_index - 1)


def sum_a_to_b(a: int, b: int) -> int:
    return (b * (b + 1) - a * (a - 1)) // 2


def solve_part_two(data: str) -> int:
    return 0


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
