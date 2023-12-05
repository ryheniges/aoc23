# https://adventofcode.com/2023/day/
from timeit import default_timer as timer

start = timer()


# Input boilerplate
def get_input(file):
    with open(file, "r") as f:
        input = f.read().splitlines()

    return input


def part_one():
    scratchcards = get_input("input.txt")

    sum = 0

    for card in scratchcards:
        # May not be necessary, but makes cards more uniform
        card = card.replace("  ", " 0")

        # Split winners and numbers we have into two lists of ints
        winners, numbers = card.split(": ")[1].split(" | ")

        winners = [int(num) for num in winners.split(" ")]
        numbers = [int(num) for num in numbers.split(" ")]

        # Count how many numbers are winners
        ocurrences = len([i for i in numbers if i in winners])

        # If there are n winners, add 2^(n-1) to the sum
        if ocurrences:
            sum += 2 ** (ocurrences - 1)

    print(f"Part 1: {sum}")


def part_two():
    scratchcards = get_input("input.txt")

    sum = 0

    # We keep track of how many cards we have of each game, starting with 1
    card_counts = [1 for _ in range(len(scratchcards))]

    for card in scratchcards:
        # May not be necessary, but makes cards more uniform
        card = card.replace("  ", " 0")

        # Split winners and numbers we have into two lists of ints
        winners, numbers = card.split(": ")[1].split(" | ")

        winners = [int(num) for num in winners.split(" ")]
        numbers = [int(num) for num in numbers.split(" ")]

        # Count how many numbers are winners
        ocurrences = len([i for i in numbers if i in winners])

        # We'll want to add the number of cards of the current game to the next N games,
        # where N is the number of winning scenarios in the current game.
        for i in range(1, ocurrences + 1):
            card_counts[i] += card_counts[0]

        # Add the count of the current game cards to the sum, and move on
        sum += card_counts[0]
        card_counts = card_counts[1:]

    print(f"Part 2: {sum}")


part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
