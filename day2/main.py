# https://adventofcode.com/2023/day/2
from timeit import default_timer as timer

start = timer()


# Input boilerplate
def get_input(file):
    with open(file, "r") as f:
        input = f.read().splitlines()

    return input


def part_one():
    games = get_input("input.txt")

    # There are 12 red cubes, 13 green cubes, and 14 blue cubes
    game_rules = {"red": 12, "green": 13, "blue": 14}

    # Track the sum of the indicies of valid games
    sum = 0

    # Loop through each game and determine if any break the "rules"
    for game in games:
        game_isvalid = True

        game_id_str, draws = game.split(": ")
        game_id = int(game_id_str.split(" ")[1])

        for draw in draws.split("; "):  # e.g. draw = "4 red, 1 green, 7 blue"
            for cubes in draw.split(", "):  # e.g. cubes = "4 red"
                count, color = cubes.split(" ")
                count = int(count)

                if count > game_rules[color]:
                    # If the game is impossible, break out of the loops
                    # and don't add the game id to the sum.
                    game_isvalid = False
                    break

            if not game_isvalid:
                break

        if game_isvalid:
            sum += game_id

    print(f"Part 1: {sum}")


def part_two():
    games = get_input("input.txt")

    # Track the sum of the "power" of minimum sets
    sum = 0

    # Loop through each game
    for game in games:
        # Track the minimum set of cubes for a game
        min_set = {"red": 0, "green": 0, "blue": 0}

        game_id_str, draws = game.split(": ")
        game_id = int(game_id_str.split(" ")[1])

        for draw in draws.split("; "):  # e.g. draw = "4 red, 1 green, 7 blue"
            for cubes in draw.split(", "):  # e.g. cubes = "4 red"
                count, color = cubes.split(" ")
                count = int(count)

                # If there are more cubes in this draw than is recorded
                # in min_set for a given color, update the value
                if count > min_set[color]:
                    min_set[color] = count

        power = min_set["red"] * min_set["green"] * min_set["blue"]

        sum += power

    print(f"Part 2: {sum}")


part_one()
part_two()

end = timer()

print(f"Time elapsed: {end - start}")
