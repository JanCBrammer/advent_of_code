"""

--- Notes ---

"""
from pathlib import Path


def parse_input(input_path: str) -> str:

    return Path(input_path).read_text()


def find_bar(foo: str) -> int:

    return 42


def solve_part1(input_path: str):

    print(f"Part 1:\n...\n")


def solve_part2(input_path: str):

    print(f"Part 2:\n...\n")


if __name__ == "__main__":

    solve_part1(f"{Path(__file__).parts[-2]}/input.txt")
    solve_part2(f"{Path(__file__).parts[-2]}/input.txt")
