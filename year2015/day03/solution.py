"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location,
and then an elf at the North Pole calls him via radio and tells him where to move next.
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once.
How many houses receive at least one present?

For example:

- > delivers presents to 2 houses: one at the starting location, and one to the east.
- ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
- ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

- ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
- ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
- ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

--- Notes ---

"""
from pathlib import Path


def parse_input(input_path: str) -> str:
    return Path(input_path).read_text()


def track_visited_houses(directions: str) -> set[tuple[int, ...]]:
    current_location = {"x": 0, "y": 0}
    visited_houses = set([tuple([0, 0])])

    for direction in directions:
        match direction:
            case "^":
                current_location["y"] += 1
            case "v":
                current_location["y"] -= 1
            case ">":
                current_location["x"] += 1
            case "<":
                current_location["x"] -= 1
        visited_houses.add(tuple(current_location.values()))

    return visited_houses


def track_visited_houses_robosanta(directions: str) -> set[tuple[int, ...]]:
    current_location_santa = {"x": 0, "y": 0}
    current_location_robosanta = {"x": 0, "y": 0}
    visited_houses = set([tuple([0, 0])])

    for i, direction in enumerate(directions):
        current_location = (
            current_location_santa if i % 2 == 0 else current_location_robosanta
        )
        match direction:
            case "^":
                current_location["y"] += 1
            case "v":
                current_location["y"] -= 1
            case ">":
                current_location["x"] += 1
            case "<":
                current_location["x"] -= 1
        visited_houses.add(tuple(current_location.values()))

    return visited_houses


def solve_part1(input_path: str):
    directions = parse_input(input_path)
    visited_houses = track_visited_houses(directions)

    print(f"Part 1:\n{len(visited_houses)} received at least one present.\n")


def solve_part2(input_path: str):
    directions = parse_input(input_path)
    visited_houses = track_visited_houses_robosanta(directions)

    print(f"Part 2:\n{len(visited_houses)} received at least one present.\n")


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
