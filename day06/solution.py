"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year,
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year,
Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction;
the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
The instructions include whether to `turn on`, `turn off`, or `toggle` various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive;
a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

- `turn on 0,0 through 999,999` would turn on (or leave on) every light.
- `toggle 0,0 through 999,0` would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
- `turn off 499,499 through 500,500` would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more.
The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

--- Notes ---

"""
from pathlib import Path
from itertools import product


def parse_input(input_path: str) -> tuple[str, tuple[tuple[int]]]:

    with Path(input_path).open() as file:
        for instruction in file:
            instruction = instruction.split()
            if len(instruction) == 5:
                instruction.pop(0)
            instruction.remove("through")
            mode = instruction.pop(0)
            coordinates = tuple(
                tuple(int(c) for c in pair.split(",")) for pair in instruction
            )

            yield mode, coordinates


def parse_coordinates(coordinates: tuple[str, tuple[tuple[int]]]) -> tuple[range]:

    rows = range(coordinates[0][0], coordinates[1][0] + 1)
    cols = range(coordinates[0][1], coordinates[1][1] + 1)

    return rows, cols


def change_light_state(
    mode: str, coordinates: tuple, light_grid: list[list[bool]]
) -> list[list[bool]]:
    """Returns mutated light grid."""

    for row, col in product(*parse_coordinates(coordinates)):
        match mode:
            case "on":
                light_grid[row][col] = True
            case "off":
                light_grid[row][col] = False
            case "toggle":
                light_grid[row][col] = not light_grid[row][col]

    return light_grid


def change_light_brightness(
    mode: str, coordinates: tuple, light_grid: list[list[bool]]
) -> list[list[bool]]:
    """Returns mutated light grid."""

    for row, col in product(*parse_coordinates(coordinates)):
        match mode:
            case "on":
                light_grid[row][col] += 1
            case "off":
                light_grid[row][col] -= 1
                if light_grid[row][col] < 0:
                    light_grid[row][col] = 0
            case "toggle":
                light_grid[row][col] += 2

    return light_grid


def solve_part1(input_path: str):

    light_grid = [[False] * 1000 for _ in range(1000)]
    for mode, coordinates in parse_input(input_path):
        change_light_state(mode, coordinates, light_grid)

    n_lit_lights = sum(sum(row) for row in light_grid)

    print(f"Part 1:\n{n_lit_lights} lights are lit after the final instruction.\n")


def solve_part2(input_path: str):

    light_grid = [[0] * 1000 for _ in range(1000)]
    for mode, coordinates in parse_input(input_path):
        change_light_brightness(mode, coordinates, light_grid)

    total_brightness = sum(sum(row) for row in light_grid)

    print(
        f"Part 2:\nAfter the final instruction, the lights have a total brightness of {total_brightness}.\n"
    )


if __name__ == "__main__":

    solve_part1(f"{Path(__file__).parts[-2]}/input.txt")
    solve_part2(f"{Path(__file__).parts[-2]}/input.txt")
