"""
--- Day 8: Two-Factor Authentication ---
You come across a door implementing what you can only assume is an implementation
of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk).
Then, it displays a code on a little screen, and you type that code on a keypad.
Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart
and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen;
these instructions are your puzzle input.
The screen is `50` pixels wide and `6` pixels tall, all of which start off,
and is capable of three somewhat peculiar operations:

- `rect AxB` turns on all of the pixels in a rectangle at the top-left of the screen which is `A` wide and `B` tall.
- `rotate row y=A by B` shifts all of the pixels in row `A` (0 is the top row) right by `B` pixels.
    Pixels that would fall off the right end appear at the left end of the row.
- `rotate column x=A by B` shifts all of the pixels in column `A` (0 is the left column) down by `B` pixels.
    Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

- `rect 3x2` creates a small rectangle in the top-left corner:

```
###....
###....
.......
```

`rotate column x=1 by 1` rotates the second column down by one pixel:

```
#.#....
###....
.#.....
```

`rotate row y=0 by 4` rotates the top row right by four pixels:

```
....#.#
###....
.#.....
```

`rotate column x=1 by 1` again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

```
.#..#.#
#.#....
.#.....
```

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market.
That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card,
if the screen did work, how many pixels should be lit?

--- Part Two ---
You notice that the screen is only capable of displaying capital letters;
in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

--- Notes ---

"""

from pathlib import Path
from typing import Generator


def parse_input(input_path: str) -> Generator[str, None, None]:
    with Path(input_path).open() as file:
        for operation in file:
            yield operation.strip()

    return None


def switch_on_rect(
    width: int, height: int, screen: list[list[bool]]
) -> list[list[bool]]:
    for row in range(height):
        for column in range(width):
            screen[row][column] = True

    return screen


def rotate_row(row: int, shift: int, screen: list[list[bool]]) -> list[list[bool]]:
    shift = shift % len(screen[row])
    screen[row] = screen[row][-shift:] + screen[row][:-shift]

    return screen


def rotate_column(
    column: int, shift: int, screen: list[list[bool]]
) -> list[list[bool]]:
    shift = shift % len(screen)
    column_values = [row[column] for row in screen]
    column_values = column_values[-shift:] + column_values[:-shift]
    for row, value in enumerate(column_values):
        screen[row][column] = value

    return screen


def run_operations(operations: Generator[str, None, None]) -> list[list[bool]]:
    screen: list[list[bool]] = [[False for _ in range(50)] for _ in range(6)]
    for operation in operations:
        if "rect" in operation:
            width, height = operation.split()[1].split("x")
            screen = switch_on_rect(int(width), int(height), screen)
        elif "rotate row" in operation:
            _, _, row, _, shift = operation.split()
            screen = rotate_row(int(row.split("=")[-1]), int(shift), screen)
        elif "rotate column" in operation:
            _, _, column, _, shift = operation.split()
            screen = rotate_column(int(column.split("=")[-1]), int(shift), screen)
        else:
            raise ValueError(f"Invalid operation: {operation}")

    return screen


def solve(input_path: str):
    final_screen = run_operations(parse_input(input_path))
    print(
        f"Part 1:\n{sum(sum(row) for row in final_screen)} pixels are lit on the screen.\n"
    )

    print("Part 2:\nThe screen displays:")
    for row in final_screen:
        print("".join("#" if pixel else "." for pixel in row))


if __name__ == "__main__":
    solve(f"{Path(__file__).parent}/input.txt")
