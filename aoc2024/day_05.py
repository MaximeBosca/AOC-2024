from aoc2024.commons import load_data, time_function, beautify_time_ns

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
    # This is a simple insert sort with a twist, not very efficient but easy to implement (kinda)
    # We have a twist because we have a compare() method that can return ? or "can't compare".
    # If no rules exist concerning our two pages. Case is partially dalt with in this sort (see 'TODO')

    # First page is sorted by default
    reordered = [update[0]]
    # All other pages are not sorted
    unknown = update[1:].copy()
    while len(unknown) != 0:
        # Let's sort page, first of the unsorted pages
        page = unknown.pop(0)
        # Get the pages before and after current page from the rules
        pages_before = rules_before.setdefault(page, [])
        pages_after = rules_after.setdefault(page, [])
        # Compare current page to already sorted pages
        for index, other in enumerate(reordered):
            is_other_before = other in pages_before
            is_other_after = other in pages_after
            if (not is_other_before) and (not is_other_after):
                # Don't know how to place page with the current sorted other
                # We place the page back at the end of unknown pages
                # TODO : What if we already have sorted 1, 2, 3 we get 4, we have the rules 3|4 but not 2|4 ?
                #  might be an infinite loop right there..
                #  Did not need it for the challenge tho.
                unknown.append(page)
                break
            if is_other_after:
                # First time we find
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
    result, time_ns = time_function(solve_part_one, data)
    print('Part one solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))
    result, time_ns = time_function(solve_part_two, data)
    print('Part two solved in {0}. Result is {1}'.format(beautify_time_ns(time_ns), result))


if __name__ == '__main__':
    main()
