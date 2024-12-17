from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '11'


def apply_rules(number: int) -> list[int]:
    if number == 0:
        return [1]
    number_str = str(number)
    if len(number_str) % 2 == 0:
        left, right = number_str[:len(number_str) // 2], number_str[len(number_str) // 2:]
        return [int(left), int(right)]
    return [number * 2024]


def blink(numbers: list[int], number_of_blinks: int, max_number_of_blinks: int) -> int:
    if number_of_blinks == max_number_of_blinks:
        return len(numbers)
    stones = 0
    for number in numbers:
        new_numbers = apply_rules(number)
        stones += blink(new_numbers, number_of_blinks + 1, max_number_of_blinks)
    return stones


def get_final_occurrences(stone_occurrences: dict[int, int]) -> int:
    return sum(stone_occurrences.values())


def blink_occurences(stone_occurrences: dict[int, int], number_of_blinks: int, max_number_of_blinks: int) -> int:
    if number_of_blinks == max_number_of_blinks:
        return get_final_occurrences(stone_occurrences)
    new_stones = dict()
    for number, occurrence in stone_occurrences.items():
        new_numbers = apply_rules(number)
        for n in new_numbers:
            if n not in new_stones:
                new_stones[n] = 0
            new_stones[n] += occurrence
    return blink_occurences(new_stones, number_of_blinks + 1, max_number_of_blinks)


def solve_part_one(data: str) -> int:
    numbers = parse_initial_occurrences(data)
    return blink_occurences(numbers, 0, 25)


def solve_part_two(data: str) -> int:
    numbers = parse_initial_occurrences(data)
    return blink_occurences(numbers, 0, 75)


def parse_initial_numbers(data: str) -> list[int]:
    return [int(number_str.strip()) for number_str in data.strip().split(" ")]


def parse_initial_occurrences(data: str) -> dict[int, int]:
    stones = dict()
    for number_str in data.strip().split(" "):
        number = int(number_str)
        if number not in stones:
            stones[number] = 0
        stones[number] += 1
    return stones


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
