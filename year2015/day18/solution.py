"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident (day06), the fire code has gotten stricter:
now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration.
With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input).
A `#` means "on", and a `.` means "off".

Then, animate your grid in steps,
where each step decides the next configuration based on the current one.
Each light's next state (either on or off) depends on its current state
and the current states of the eight lights adjacent to it (including diagonals).
Lights on the edge of the grid might have fewer than eight neighbors;
the missing ones always count as "off".

For example, in a simplified 6x6 grid,
the light marked `A` has the neighbors numbered `1` through `8`,
and the light marked `B`, which is on an edge, only has the neighbors marked `1` through `5`:

```
1B5...
234...
......
..123.
..8A4.
..765.
```

The state a light should have next is based on its current state (on or off)
plus the number of neighbors that are on:

- A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
- A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously;
they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

```
Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
```

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration,
how many lights are on after 100 steps?

--- Part Two ---
You flip the instructions over;
Santa goes on to point out that this is all just an implementation of Conway's Game of Life.
At least, it was, until you notice that something's wrong with the grid of lights you bought:
four lights, one in each corner, are stuck on and can't be turned off.
The example above will actually run like this:

```
Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
```

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state,
how many lights are on after 100 steps?


--- Notes ---

"""
from pathlib import Path
from typing import Final


def parse_input(input_path: str) -> tuple[bool, ...]:
    with Path(input_path).open() as file:
        return tuple(light.strip() == "#" for line in file for light in line.strip())


def _find_light_neighbors(light: int, n_cols: int, n_neighbors: int) -> tuple[int, ...]:
    neighbors = [
        light - n_cols - 1,
        light - n_cols,
        light - (n_cols - 1),
        light - 1,
        light + 1,
        light + n_cols - 1,
        light + n_cols,
        light + n_cols + 1,
    ]

    if light % n_cols == 0:  # first row index
        neighbors = [
            light - n_cols,
            light - (n_cols - 1),
            light + 1,
            light + n_cols,
            light + n_cols + 1,
        ]

    elif light % n_cols == n_cols - 1:  # last row index
        neighbors = [
            light - n_cols - 1,
            light - n_cols,
            light - 1,
            light + n_cols - 1,
            light + n_cols,
        ]

    return tuple(n_i for n_i in neighbors if 0 <= n_i <= n_neighbors - 1)


def map_light_neighbors(
    n_cols: int = 100, n_rows: int = 100
) -> tuple[tuple[int, ...], ...]:
    """List neighbor indices for each light.

    The indices refer to a vector (1D) representation of the grid / matrix (2D).
    The 2D kernel that is used to mark the neighbors in the grid
    is transformed to a 1D kernel:

    0   1   2   3
    4   5   6   7
    8   9   10  11
    12  13  14  15

    When transforming the grid to a vector, the neighbors of each light
    can be found with a mask / kernel (`X` marks a neighbor) that we
    slide along the vector. The kernel is centered on a light and extends
    by n_columns + 1 to either side.

    _   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
    0       X           X   X
    1   X       X       X   X   X
    2       X       X       X   X   X
    3           X               X   X
    4   X   X               X           X   X
    5   X   X   X       X       X       X   X   X
    6       X   X   X       X       X       X   X   X
    7           X   X           X               X   X
    8                   X   X               X           X   X
    9                   X   X   X       X       X       X   X   X
    10                      X   X   X       X       X       X   X   X
    11                          X   X           X               X   X
    12                                  X   X               X
    13                                  X   X   X       X       X
    14                                      X   X   X       X       X
    15
    """
    n_neighbors = n_cols * n_rows

    return tuple(
        _find_light_neighbors(light, n_cols, n_neighbors)
        for light in range(n_neighbors)
    )


def compute_light_state(
    light: int, lights: tuple[bool, ...], light_neighbors: tuple[int, ...]
) -> bool:
    light_on = lights[light]
    n_lit_neighbors = sum(lights[n] for n in light_neighbors)

    light_state = False

    if light_on and n_lit_neighbors in {2, 3}:
        light_state = True

    if not light_on and n_lit_neighbors == 3:
        light_state = True

    return light_state


def switch_on_grid_corners(
    lights: tuple[bool, ...], n_cols: int = 100, n_rows: int = 100
) -> tuple[bool, ...]:
    corners = {0, n_cols - 1, n_cols * n_rows - n_cols, n_cols * n_rows - 1}

    return tuple(True if i in corners else light for i, light in enumerate(lights))


def solve(input_path: str):
    LIGHT_NEIGHBORS: Final[tuple[tuple[int, ...], ...]] = map_light_neighbors()
    n_steps = 100

    lights = parse_input(input_path)
    for _ in range(n_steps):
        lights = tuple(
            compute_light_state(light, lights, light_neighbors)
            for light, light_neighbors in enumerate(LIGHT_NEIGHBORS)
        )
    print(f"Part 1:\nAfter {n_steps} steps, {sum(lights)} lights are switched on.\n")

    lights = switch_on_grid_corners(parse_input(input_path))
    for _ in range(n_steps):
        lights = tuple(
            compute_light_state(light, lights, light_neighbors)
            for light, light_neighbors in enumerate(LIGHT_NEIGHBORS)
        )
        lights = switch_on_grid_corners(lights)
    print(
        f"Part 2:\nAfter {n_steps} steps, {sum(lights)} lights are switched on when the four corners are always in the 'on' state.\n"
    )


if __name__ == "__main__":
    solve(f"{Path(__file__).parent}/input.txt")
