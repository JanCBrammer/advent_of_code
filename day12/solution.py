"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format.
That's where you come in.

They have a JSON document which contains a variety of things:
- arrays ([1,2,3]),
- objects ({"a":1, "b":2}),
- numbers, and
- strings.
Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

- `[1,2,3]` and `{"a":2,"b":4}` both have a sum of 6.
- `[[[3]]]` and `{"a":{"b":4},"c":-1}` both have a sum of 3.
- `{"a":[-1,1]}` and `[-1,{"a":1}]` both have a sum of 0.
- `[]` and `{}` both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red".
Do this only for objects ({...}), not arrays ([...]).

- `[1,2,3]` still has a sum of 6.
- `[1,{"c":"red","b":2},3]` now has a sum of 4, because the middle object is ignored.
- `{"d":"red","e":[1,2,3,4],"f":5}` now has a sum of 0, because the entire structure is ignored.
- `[1,"red",5]` has a sum of 6, because "red" in an array has no effect.

--- Notes ---

"""
import json
import re
from pathlib import Path
from typing import Union, Generator


def parse_input(input_path: str) -> str:

    return Path(input_path).read_text()


def add_numbers(document: str) -> int:

    return sum(int(number) for number in re.findall(r"[-]?[0-9]+", document))


def add_numbers_conditionally(json_data: Union[str, int, list, dict]) -> Generator:

    if isinstance(json_data, dict):
        if "red" not in json_data.values():
            yield from add_numbers_conditionally(list(json_data.values()))

    elif isinstance(json_data, list):
        for data in json_data:
            yield from add_numbers_conditionally(data)

    elif isinstance(json_data, int):
        yield json_data


def solve_part1(input_path: str):

    print(
        f"Part 1:\nThe sum of all numbers in the document is {add_numbers(parse_input(input_path))}.\n"
    )


def solve_part2(input_path: str):

    document = parse_input(input_path)
    json_document = json.loads(document)

    print(
        "Part 2:\nExcluding objects containig 'red',"
        " the sum of all numbers in the document is"
        f" {sum(add_numbers_conditionally(json_document))}.\n"
    )


if __name__ == "__main__":

    solve_part1(f"{Path(__file__).parts[-2]}/input.txt")
    solve_part2(f"{Path(__file__).parts[-2]}/input.txt")
