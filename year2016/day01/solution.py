"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements,
and the clock's oscillator is regulated by stars.
Unfortunately, the stars have been stolen... by the Easter Bunny.
To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles.
Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get -
the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here,
and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North.
Then, follow the provided sequence: either turn left (`L`) or right (`R`) 90 degrees,
then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot,
though, so you take a moment and work out the destination.
Given that you can only walk on the street grid of the city,
how far is the shortest path to the destination?

For example:
    - Following `R2, L3` leaves you `2` blocks East and `3` blocks North, or `5` blocks away.
    - `R2, R2, R2` leaves you `2` blocks due South of your starting position, which is `2` blocks away.
    - `R5, L5, R5, R3` leaves you `12` blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document.
Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are `R8, R4, R4, R8`,
the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?


--- Notes ---

"""
from pathlib import Path
from typing import Final


FACING_DIRECTIONS: Final[dict[str, dict[str, str]]] = {
    "L": {"N": "W", "E": "N", "S": "E", "W": "S"},
    "R": {"N": "E", "E": "S", "S": "W", "W": "N"},
}

OPERATORS: Final[dict[str, dict[str, int]]] = {
    "L": {"N": -1, "E": 1, "S": 1, "W": -1},
    "R": {"N": 1, "E": -1, "S": -1, "W": 1},
}


def trace_path_to_hq(instructions: str) -> list[tuple[int, int]]:
    x: int = 0
    y: int = 0
    facing_direction: str = "N"
    path: list[tuple[int, int]] = [(x, y)]

    for instruction in instructions.split(", "):
        turning_direction: str = instruction[0]
        n_blocks: int = int(instruction[1:])
        operator: int = OPERATORS[turning_direction][facing_direction]

        for _ in range(1, n_blocks + 1):  # Interpolate path between turning points.
            if facing_direction in ["N", "S"]:
                x += operator
            else:
                y += operator
            path.append((x, y))

        facing_direction = FACING_DIRECTIONS[turning_direction][facing_direction]

    return path


def find_first_recurring_location(path: list[tuple[int, int]]) -> tuple[int, int]:
    # Requires full path, not only turning points.
    while path:
        location: tuple[int, int] = path.pop(0)
        if location in path:
            return location

    return location


def compute_manhattan_distance_from_origin(location: tuple[int, int]) -> int:
    (x, y) = location

    return abs(x) + abs(y)


def solve_part1(input_path: str):
    hq_location: tuple[int, int] = trace_path_to_hq(Path(input_path).read_text())[-1]
    print(
        f"Part 1:\nThe Easter Bunny HQ is {compute_manhattan_distance_from_origin(hq_location)} blocks away.\n"
    )


def solve_part2(input_path: str):
    first_recurring_location: tuple[int, int] = find_first_recurring_location(
        trace_path_to_hq(Path(input_path).read_text())
    )
    print(
        f"Part 2:\nThe first location that's visited twice is {compute_manhattan_distance_from_origin(first_recurring_location)} blocks away.\n"
    )


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
