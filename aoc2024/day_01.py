from aoc2024.commons import load_data, time_function, beautify_time_ns

DAY_NUMBER = '01'


def solve_part_one(data: str) -> int:
    return 0


def solve_part_two(data: str) -> int:
    right_list = []
    left_list = []
    lines = data.strip().split('\n')
    for line in lines:
        left, right = line.strip().split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    left_list.sort()
    right_list.sort()

    similarity_score = 0

    previous_number = 0
    previous_occurrences = 0
    right_index = 0
    for i in range(len(left_list)):
        current_number = left_list[i]
        if current_number == previous_number:
            similarity_score += previous_occurrences * previous_number
            continue
        occurrences = 0
        while right_index < len(right_list) and right_list[right_index] <= current_number:
            right_number = right_list[right_index]
            if right_number == current_number:
                occurrences += 1
            right_index += 1

        similarity_score += previous_occurrences * previous_number

        previous_number = current_number
        previous_occurrences = occurrences

    return similarity_score


def main():
    data = load_data(DAY_NUMBER)
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
