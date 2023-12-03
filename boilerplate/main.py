# https://adventofcode.com/2023/day/
from timeit import default_timer as timer

start = timer()


# Input boilerplate
def get_input(file):
    with open(file, "r") as f:
        input = f.read().splitlines()

    return input


def part_one():
    _ = get_input("sample.txt")

    # print(f"Part 1: {_}")


def part_two():
    _ = get_input("sample.txt")

    # print(f"Part 2: {_}")


part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
