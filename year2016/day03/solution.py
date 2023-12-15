"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly,
you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ.
This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but...
`5 10 25`? Some of these aren't triangles.
You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side.
For example, the "triangle" given above is impossible,
because `5 + 10` is not larger than `25`.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents,
it occurs to you that triangles are specified in groups of three vertically.
Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification,
numbers with the same hundreds digit would be part of the same triangle:

```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```

In your puzzle input, and instead reading by columns,
how many of the listed triangles are possible?

--- Notes ---

"""
from pathlib import Path
from typing import Generator
from itertools import combinations, batched


def parse_input_part1(input_path: str) -> Generator[tuple[int, int, int], None, None]:
    with Path(input_path).open() as input_file:
        for triangle_specification in input_file:
            yield tuple(
                int(i) for i in triangle_specification.split()
            )  # type: ignore[misc]

    return None


def parse_input_part2(input_path: str) -> Generator[tuple[int, int, int], None, None]:
    with Path(input_path).open() as input_file:
        for triangle_specification_triple in batched(input_file, 3):
            for triangle_specification in zip(  # transpose with zip
                *(
                    tuple(int(i) for i in line.split())
                    for line in triangle_specification_triple
                )
            ):
                yield triangle_specification  # type: ignore[misc]

    return None


def triangle_is_valid(triangle_specification: tuple[int, int, int]) -> bool:
    indices: set[int] = {0, 1, 2}

    for sum_indices in combinations(indices, 2):
        (remaining_index,) = indices - set(sum_indices)
        if (
            sum(triangle_specification[i] for i in sum_indices)
            <= triangle_specification[remaining_index]
        ):
            return False

    return True


def filter_valid_triangles(
    triangle_specifications: Generator[tuple[int, int, int], None, None]
) -> list[tuple[int, int, int]]:
    return [
        triangle_specification
        for triangle_specification in triangle_specifications
        if triangle_is_valid(triangle_specification)
    ]


def solve_part1(input_path: str):
    valid_triangles = filter_valid_triangles(parse_input_part1(input_path))
    print(f"Part 1:\n{len(valid_triangles)} of the listed triangles are valid.\n")


def solve_part2(input_path: str):
    valid_triangles = filter_valid_triangles(parse_input_part2(input_path))
    print(f"Part 2:\n{len(valid_triangles)} of the listed triangles are valid.\n")


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
