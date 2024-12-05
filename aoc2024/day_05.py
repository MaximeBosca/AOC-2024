from aoc2024.commons import load_data

DAY_NUMBER = '05'


def separate_input(data: str) -> tuple[list[str], list[str]]:
    lines = data.strip().split('\n')
    sep_index = lines.index('')
    return lines[:sep_index], lines[sep_index + 1:]


def load_rules_after(lines: list[str]) -> dict[int, list[int]]:
    rules = dict()
    for line in lines:
        left, right = line.strip().split('|')
        rules.setdefault(int(left), []).append(int(right))
    return rules


def load_all_rules(lines: list[str]) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    rules_before = dict()
    rules_after = dict()
    for line in lines:
        left, right = line.strip().split('|')
        rules_after.setdefault(int(left), []).append(int(right))
        rules_before.setdefault(int(right), []).append(int(left))
    return rules_before, rules_after


def map_update_string(update_str: str) -> list[int]:
    return [int(page.strip()) for page in update_str.split(',')]


def is_correct_order(update: list[int], rules: dict[int, list[int]]) -> bool:
    for index, page in enumerate(update):
        page_rules = rules.setdefault(page, [])
        for other in update[:index]:
            if other in page_rules:
                return False
    return True


def get_middle_page(update: list[int]) -> int:
    return update[(len(update) // 2)]


def solve_part_one(data: str) -> int:
    rules_str, updates_str = separate_input(data)
    rules = load_rules_after(rules_str)
    return sum(
        map(get_middle_page,
            filter(lambda update: is_correct_order(update, rules),
                   map(map_update_string,
                       updates_str)
                   )
            )
    )


def reorder(update: list[int], rules_before: dict[int, list[int]], rules_after: dict[int, list[int]]) -> list[int]:
    unknown = update[1:].copy()
    reordered = [update[0]]
    while len(unknown) != 0:
        page = unknown.pop(0)
        pages_before = rules_before.setdefault(page, [])
        pages_after = rules_after.setdefault(page, [])
        for index, other in enumerate(reordered):
            is_other_before = other in pages_before
            is_other_after = other in pages_after
            if (not is_other_before) and (not is_other_after):
                unknown.append(page)
                break
            if is_other_after:
                reordered.insert(index, page)
                break
            if index == len(reordered) - 1:
                reordered.append(page)
                break
    return reordered


def solve_part_two(data: str) -> int:
    rules_str, updates_str = separate_input(data)
    rules_before, rules_after = load_all_rules(rules_str)
    return sum(
        map(get_middle_page,
            map(lambda update: reorder(update, rules_before, rules_after),
                filter(lambda update: not is_correct_order(update, rules_after),
                       map(map_update_string,
                           updates_str)
                       )
                )
            )
    )


def main():
    data = load_data(DAY_NUMBER)
    print('Part one solved :', solve_part_one(data))
    print('Part two solved :', solve_part_two(data))


if __name__ == '__main__':
    main()
