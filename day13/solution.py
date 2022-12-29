"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along! This year, you resolve, will be different.
You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited
and the amount their happiness would increase or decrease
if they were to find themselves sitting next to each other person.
You have a circular table that will be just big enough to fit everyone comfortably,
and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned,
and you calculate their potential happiness as follows:

```
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
```

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much),
but David would gain 46 happiness units (because Alice is such a good listener),
for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54).
Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7)
and David (Carol gains 55, David gains 41). The arrangement looks like this:

```
     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
```
After trying every other seating arrangement in this hypothetical scenario,
you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself.
At this point, you're pretty apathetic toward the whole thing,
and your happiness wouldn't really go up or down regardless of who you sit next to.
You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

--- Notes ---

"""
from pathlib import Path
from collections import defaultdict
from operator import neg
from itertools import permutations, pairwise


def parse_input(input_path: str) -> dict[str, dict[str, int]]:

    happiness_changes = defaultdict(dict)

    with Path(input_path).open() as file:
        for line in file:
            split_line = line.strip().split()
            change = (
                neg(int(split_line[3]))
                if split_line[2] == "lose"
                else int(split_line[3])
            )
            happiness_changes[split_line[0]].update({split_line[-1][:-1]: change})

    return happiness_changes


def compute_happiness(
    seating_arrangement: tuple[str, ...],
    happiness_changes: dict[str, dict[str, int]],
) -> int:

    happiness = 0
    for attendee_i, attendee_j in pairwise(
        list(seating_arrangement) + [seating_arrangement[0]]
    ):
        happiness += happiness_changes[attendee_i][attendee_j]
        happiness += happiness_changes[attendee_j][attendee_i]

    return happiness


def find_optimal_seating_arrangement(
    happiness_changes: dict[str, dict[str, int]]
) -> int:

    max_happiness = float("-inf")

    for seating_arrangement in permutations(happiness_changes.keys()):
        happiness = compute_happiness(seating_arrangement, happiness_changes)
        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


def solve_part1(input_path: str):

    happiness_changes = parse_input(input_path)
    max_happiness = find_optimal_seating_arrangement(happiness_changes)

    print(
        f"Part 1:\nThe total change in happiness for the optimal seating arrangement is {max_happiness}.\n"
    )


def solve_part2(input_path: str):

    happiness_changes = parse_input(input_path)
    for attendee in list(happiness_changes):
        happiness_changes["Jan"].update({attendee: 0})
        happiness_changes[attendee].update({"Jan": 0})
    max_happiness = find_optimal_seating_arrangement(happiness_changes)

    print(
        f"Part 2:\nThe total change in happiness for the optimal seating arrangement is {max_happiness}.\n"
    )


if __name__ == "__main__":

    solve_part1(f"{Path(__file__).parts[-2]}/input.txt")
    solve_part2(f"{Path(__file__).parts[-2]}/input.txt")
