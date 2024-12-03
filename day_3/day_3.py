import re

REGEXP = "(mul\\(\\d{1,3},\\d{1,3}\\))|(do\\(\\))|(don't\\(\\))"


def process_command(command: str) -> int:
    left_number, right_number = command[4:-1].split(',')
    return int(left_number) * int(right_number)


def main():
    total = 0
    with open('input.txt', 'r') as file:
        data = file.read()
        do = True
        commands = re.findall(REGEXP, data)
        for mul_command, do_command, dont_command in commands:
            if do_command:
                do = True
                continue
            if dont_command:
                do = False
                continue
            if do:
                total += process_command(mul_command)
    print(total)


if __name__ == '__main__':
    main()
