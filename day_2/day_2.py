def valid_levels(previous_level: int, current_level: int, increasing: bool):
    difference = previous_level - current_level
    if (increasing and difference >= 0) or (not increasing and difference <= 0):
        return False
    if abs(difference) > 3:
        return False
    return True


def is_report_safe(report: list[int]) -> bool:
    if len(report) <= 2:
        return True
    increasing = report[0] - report[1] < 0
    fails = 0
    last_invalid = -1
    tmp_last_invalid = -1
    for index, current_level in enumerate(report):
        last_invalid = tmp_last_invalid
        if index == 0:
            continue
        if valid_levels(report[index - 1], current_level, increasing):
            continue
        fails += 1
        tmp_last_invalid = index
        if index == len(report) - 1 and fails == 1:
            return True

        if index == 1 or index == 2:
            increasing = report[len(report) - 2] - report[len(report) - 1] < 0

        if index == 1:
            continue

        if index == 2:
            if (valid_levels(report[index - 2], current_level, increasing)
                    or valid_levels(report[index - 1], current_level, increasing)):
                continue

        if not valid_levels(report[index - 2], current_level, increasing):
            return False

        if fails == 1:
            continue
        if fails > 2:
            return False
        if last_invalid != index - 1:
            return False
    return True


def main():
    safe_reports = 0
    with open('input.txt', 'r') as file:
        for line in file:
            report_str = line.strip().split(" ")
            safe_reports += 1 if is_report_safe([int(level) for level in report_str]) else 0
            if (not is_report_safe([int(level) for level in report_str])):
                print(report_str)
    print(safe_reports)


if __name__ == '__main__':
    main()
