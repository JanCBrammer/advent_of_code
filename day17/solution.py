"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time.
To fit it all into your refrigerator, you'll need to move it into smaller containers.
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
If you need to store 25 liters, there are four ways to do it:

- 15 and 10
- 20 and 5 (the first 5)
- 20 and 5 (the second 5)
- 15, 5, and 5

Filling all containers entirely,
how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives!
The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog.
How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two.
There were three ways to use that many containers, and so the answer there would be 3.

--- Notes ---

"""
from pathlib import Path
from itertools import combinations


def parse_input(input_path: str) -> tuple[int, ...]:

    return tuple(int(i) for i in Path(input_path).read_text().splitlines())


def find_container_combinations(
    containers: tuple[int, ...], target_volume: int
) -> list[tuple[int, ...]]:

    container_combinations = []

    for n_containers in range(len(containers)):
        for combination in combinations(containers, n_containers + 1):
            if sum(combination) == target_volume:
                container_combinations.append(combination)

    return container_combinations


def solve(input_path: str):

    containers = parse_input(input_path)
    container_combinations = find_container_combinations(containers, 150)

    n_combinations = len(container_combinations)
    print(
        f"Part 1:\nThere are {n_combinations} different container combinations that exactly fit 150 liters.\n"
    )

    print(sorted(container_combinations, key=len))
    min_n_containers = min(len(c) for c in container_combinations)
    n_combinations = len(
        [c for c in container_combinations if len(c) == min_n_containers]
    )
    print(
        f"Part 2:\nThere are {n_combinations} different ways to fill {min_n_containers} containers with exactly 150 litres.\n"
    )


if __name__ == "__main__":

    solve(f"{Path(__file__).parts[-2]}/input.txt")
