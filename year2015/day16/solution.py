"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card.
However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue
(which you conveniently number 1 to 500, for sanity) gave you the gift.
You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine!
Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample,
as well as how many distinct kinds of those compounds there are.
According to the instructions, these are what the MFCSAM can detect:

- `children`, by human DNA age analysis.
- `cats`. It doesn't differentiate individual breeds.
- Several seemingly random breeds of dog: `samoyeds`, `pomeranians`, `akitas`, and `vizslas`.
- `goldfish`. No other kinds of fish.
- `trees`, all in one group.
- `cars`, presumably by exhaust or gasoline or something.
- `perfumes`, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM.
It beeps inquisitively at you a few times and then prints out a message on ticker tape:

```
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
```
You make a list of the things you can remember about each Aunt Sue.
Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye.
Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values
- some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many
(due to the unpredictable nuclear decay of cat dander and tree pollen),
while the pomeranians and goldfish readings indicate that there are fewer than that many
(due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?


--- Notes ---

No code is the best code: part 1 can be solved quickly by looking up the matching aunt manually.
It's Sue 213.

"""
from pathlib import Path
from typing import Iterator, Callable
from dataclasses import dataclass
from operator import eq, gt, lt


@dataclass
class AuntAttributeQuery:
    matcher: Callable
    value: int

    def match(self, query: int) -> bool:
        return self.matcher(query, self.value)


AUNT_ATTRIBUTE_QUERIES = {
    "children": AuntAttributeQuery(eq, 3),
    "cats": AuntAttributeQuery(gt, 7),
    "samoyeds": AuntAttributeQuery(eq, 2),
    "pomeranians": AuntAttributeQuery(lt, 3),
    "akitas": AuntAttributeQuery(eq, 0),
    "vizslas": AuntAttributeQuery(eq, 0),
    "goldfish": AuntAttributeQuery(lt, 5),
    "trees": AuntAttributeQuery(gt, 3),
    "cars": AuntAttributeQuery(eq, 2),
    "perfumes": AuntAttributeQuery(eq, 1),
}


def parse_input(input_path: str) -> Iterator[dict[str, int]]:
    with Path(input_path).open() as file:
        for line in file:
            aunt_attributes = dict(
                [s.strip() for s in segment.split(":")[-2:]]
                for segment in line.split(",")
            )

            yield {k: int(v) for k, v in aunt_attributes.items()}


def find_aunt(aunts: Iterator[dict[str, int]]) -> int:
    for aunt_number, aunt_attributes in enumerate(aunts):
        if match_aunt(aunt_attributes):
            return aunt_number + 1


def match_aunt(aunt_attributes: dict[str, int]) -> bool:
    return all(
        (
            AUNT_ATTRIBUTE_QUERIES[key].match(value)
            for key, value in aunt_attributes.items()
        )
    )


def solve_part2(input_path: str):
    aunts = parse_input(input_path)
    matching_aunt = find_aunt(aunts)

    print(f"Part 2:\nThe gift's from aunt Sue {matching_aunt}.\n")


if __name__ == "__main__":
    solve_part2(f"{Path(__file__).parent}/input.txt")
