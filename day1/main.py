# https://adventofcode.com/2023/day/1
from timeit import default_timer as timer

start = timer()

# Input boilerplate
def get_input(file):
    with open(file, 'r') as f:
        input = f.read().splitlines()

    return input


def part_one():
    calibration_lines = get_input('input.txt')

    # Filter the calibration lines down to a list of numeric strings
    calibration_line_digits = []
    for calibration_line in calibration_lines:
        calibration_line_digits.append(
            [char for char in calibration_line if char.isdigit()]
        )

    # Form the two digit number, convert to int, and add to sum
    sum = 0
    for digit_array in calibration_line_digits:
        sum+=int(digit_array[0]+digit_array[-1])

    print(f"Part 1: {sum}")


def part_two():
    calibration_lines = get_input('p2_sample.txt')

    # Filter the calibration lines down to a list of numeric strings
    calibration_line_digits = []
    for calibration_line in calibration_lines:
        calibration_line_digits.append(
            [char for char in calibration_line if char.isdigit()]
        )

    # Form the two digit number, convert to int, and add to sum
    sum = 0
    for digit_array in calibration_line_digits:
        sum+=int(digit_array[0]+digit_array[-1])

    print(f"Part 2: {sum}")


# part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
