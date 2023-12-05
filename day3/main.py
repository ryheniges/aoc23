# https://adventofcode.com/2023/day/
from timeit import default_timer as timer
import re
from collections import defaultdict

start = timer()


# Input boilerplate
def get_input(file):
    with open(file, "r") as f:
        input = f.read().splitlines()

    return input


def part_one():
    """
    Scan through the input one row at a time, and find all the numbers.

    Keep track of the previous and next row, so we can check later for symbols.

    Determine the index range of each number in the row, and check that range in
    the previous, current, and next row for any special characters.
    """
    engine_schematic_lines = get_input("input.txt")

    previous_line = ""  # To be overwritten after the first row
    sum = 0

    for row_index, engine_schematic_line in enumerate(engine_schematic_lines):
        try:
            next_line = engine_schematic_lines[row_index + 1]
        except IndexError:
            next_line = ""

        # Find all of the digits in this line
        # https://pynative.com/python-regex-split/
        digits = re.split(r"\D+", engine_schematic_line)
        digits = [digit for digit in digits if digit]  # Filter out empty strings

        # "index" helps solve an edge case with subsequent repeating numbers
        index = 0

        for digit in digits:
            digit_index = engine_schematic_line[index:].find(digit)
            index = index + digit_index

            # The range of the prev, current, and next rows that we will check
            # for special characters.
            check_index = [index - 1, index + len(digit)]
            # Don't go out of the range of the rows or columns
            check_index[0] = max(check_index[0], 0)
            check_index[1] = min(check_index[1], len(engine_schematic_line))

            # Make sure we search for the next digit past the current number
            index += 1

            # Remove all digits or periods
            prev_row_special_chars = re.sub(
                r"[0-9.]", "", previous_line[check_index[0] : check_index[1] + 1]
            )
            curr_row_special_chars = re.sub(
                r"[0-9.]",
                "",
                engine_schematic_line[check_index[0] : check_index[1] + 1],
            )
            next_row_special_chars = re.sub(
                r"[0-9.]", "", next_line[check_index[0] : check_index[1] + 1]
            )

            # If anything remains, include it in the sum
            if (
                prev_row_special_chars
                or curr_row_special_chars
                or next_row_special_chars
            ):
                sum += int(digit)

        previous_line = engine_schematic_line

    print(f"Part 1: {sum}")


def part_two():
    engine_schematic_lines = get_input("input.txt")

    previous_line = ""  # To be overwritten after the first row
    sum = 0

    # We want to know what gears have exactly two adjacent numbers, and know what those are.
    # 'gears' will have keys that are tuples, representing the row and column of a gear.
    # The value for a gear's coordinate tuple is a list of adjacent numbers
    gears = defaultdict(list)

    for row_index, engine_schematic_line in enumerate(engine_schematic_lines):
        try:
            next_line = engine_schematic_lines[row_index + 1]
        except IndexError:
            next_line = ""

        # Find all of the numbers in this line
        # https://pynative.com/python-regex-split/
        numbers = re.split(r"\D+", engine_schematic_line)
        numbers = [number for number in numbers if number]  # Filter out empty strings

        # "index" helps solve an edge case with subsequent repeating numbers
        index = 0

        for number in numbers:
            number_index = engine_schematic_line[index:].find(number)
            index = index + number_index

            # The range of the prev, current, and next rows that we will check
            # for gears.
            check_index = [index - 1, index + len(number)]
            # Don't go out of the range of the rows or columns
            check_index[0] = max(check_index[0], 0)
            check_index[1] = min(check_index[1], len(engine_schematic_line))

            # Determine the substrings we want to look in for gears
            prev_line_substring = previous_line[check_index[0] : check_index[1] + 1]
            curr_line_substring = engine_schematic_line[
                check_index[0] : check_index[1] + 1
            ]
            next_line_substring = next_line[check_index[0] : check_index[1] + 1]

            # Find gear coordinates in any of the surrounding characters, and record
            # the numbers adjacent to these gears
            if "*" in prev_line_substring:
                gears = get_gear_indexes(
                    gears, number, row_index - 1, index, prev_line_substring
                )

            if "*" in curr_line_substring:
                gears = get_gear_indexes(
                    gears, number, row_index, index, curr_line_substring
                )

            if "*" in next_line_substring:
                gears = get_gear_indexes(
                    gears, number, row_index + 1, index, next_line_substring
                )

            # Make sure we search for the next number past the current number
            index += 1

        previous_line = engine_schematic_line

    for schematic_ints in gears.values():
        if len(schematic_ints) == 2:
            sum += schematic_ints[0] * schematic_ints[1]

    print(f"Part 2: {sum}")


def get_gear_indexes(gears, number, row_index, column_index, substring):
    """
    Things get complicated if there are multiple "gears" in the same substring

    e.g.
    ..123..
    ..*.*..
    ..456..

    This function takes care of that
    """
    if column_index == 0:
        column_index = 1

    for idx, char in enumerate(substring):
        if char == "*":
            gear_col = column_index + idx - 1
            gears[(row_index, gear_col)].extend([int(number)])

    return gears


part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
