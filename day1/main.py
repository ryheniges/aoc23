# https://adventofcode.com/2023/day/1
from timeit import default_timer as timer

start = timer()


# Input boilerplate
def get_input(file):
    with open(file, "r") as f:
        input = f.read().splitlines()

    return input


def part_one():
    calibration_lines = get_input("input.txt")

    # Filter the calibration lines down to a list of numeric strings
    calibration_line_digits = []
    for calibration_line in calibration_lines:
        calibration_line_digits.append(
            [char for char in calibration_line if char.isdigit()]
        )

    # Form the two digit number, convert to int, and add to sum
    sum = 0
    for digit_array in calibration_line_digits:
        sum += int(digit_array[0] + digit_array[-1])

    print(f"Part 1: {sum}")


def part_two():
    calibration_lines = get_input("input.txt")

    # Used for converting strings to integers
    digit_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    sum = 0

    for calibration_line in calibration_lines:
        # If a calibration line is "two1nine", digit_array should be ["2", "1", "9"]
        digit_array = []

        for index in range(len(calibration_line)):
            """
            "Scan" through the calibration_line and validate a few substrings to see if it represents an integer.

            Substrings we're interested in will be 1, 3, 4, or 5 characters.
              - "1" = one character
              - "six" = three characters
              - "five" = four characters
              - "eight" = five characters
            """

            if calibration_line[index].isdigit():  # one character
                digit_array.append(calibration_line[index])

            if (
                calibration_line[index : index + 3] in digit_dict.keys()
            ):  # three characters
                string_digit = digit_dict[
                    calibration_line[index : index + 3]
                ]  # convert to a string 'int'
                digit_array.append(string_digit)

            if (
                calibration_line[index : index + 4] in digit_dict.keys()
            ):  # four characters
                string_digit = digit_dict[
                    calibration_line[index : index + 4]
                ]  # convert to a string 'int'
                digit_array.append(string_digit)

            if (
                calibration_line[index : index + 5] in digit_dict.keys()
            ):  # five characters
                string_digit = digit_dict[
                    calibration_line[index : index + 5]
                ]  # convert to a string 'int'
                digit_array.append(string_digit)

        # Add values for that line to the sum
        sum += int(digit_array[0] + digit_array[-1])

    print(f"Part 2: {sum}")


part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
