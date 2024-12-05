from aoc2024.commons import load_data

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
    previous_occurences = 0
    right_index = 0
    for i in range(len(left_list)):
        current_number = left_list[i]
        if current_number == previous_number:
            similarity_score += previous_occurences * previous_number
            continue
        occurences = 0
        while right_index < len(right_list) and right_list[right_index] <= current_number:
            right_number = right_list[right_index]
            if right_number == current_number:
                occurences += 1
            right_index += 1

        similarity_score += previous_occurences * previous_number

        previous_number = current_number
        previous_occurences = occurences

    return similarity_score


def main():
    data = load_data(DAY_NUMBER)
    print('Part one solved :', solve_part_one(data))
    print('Part two solved :', solve_part_two(data))


if __name__ == '__main__':
    main()
