"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door.
He sends them down a street with infinite houses numbered sequentially: `1`, `2`, `3`, `4`, `5`, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

- The first Elf (number `1`) delivers presents to every house: `1`, `2`, `3`, `4`, `5`, ....
- The second Elf (number `2`) delivers presents to every second house: `2`, `4`, `6`, `8`, `10`, ....
- Elf number `3` delivers presents to every third house: `3`, `6`, `9`, `12`, `15`, ....

There are infinitely many Elves, numbered starting with `1`.
Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

```
House 1 got 10 presents.    (1)
House 2 got 30 presents.    (1 + 2)
House 3 got 40 presents.    (1 + 3)
House 4 got 70 presents.    (1 + 2 + 4)
House 5 got 60 presents.    (1 + 5)
House 6 got 120 presents.   (1 + 2 + 3 + 6)
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
```

The first house gets `10` presents: it is visited only by Elf `1`, which delivers `1 * 10 = 10` presents.
The fourth house gets `70` presents, because it is visited by Elves `1`, `2`, and `4`, for a total of `10 + 20 + 40 = 70` presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is `36000000`.


--- Part Two ---

The Elves decide they don't want to visit an infinite number of houses.
Instead, each Elf will stop after delivering presents to 50 houses.
To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?



--- Notes ---
https://stackoverflow.com/questions/26753839/efficiently-getting-all-divisors-of-a-given-number

sigma function aka sum-of-divisors function:
https://en.wikipedia.org/wiki/Divisor_function

"""
from math import sqrt
from typing import Callable


def compute_number_of_presents_part1(house_number: int) -> int:
    number_of_presents = 0
    for elf_id in range(1, int(sqrt(house_number)) + 1):
        if not house_number % elf_id:
            number_of_presents += elf_id
            if elf_id != house_number // elf_id:
                number_of_presents += house_number // elf_id

    return number_of_presents * 10


def compute_number_of_presents_part2(house_number: int) -> int:
    number_of_presents = 0
    for elf_id in range(1, int(sqrt(house_number)) + 1):
        if not house_number % elf_id:
            number_of_presents += elf_id if house_number <= 50 * elf_id else 0
            if elf_id != house_number // elf_id:
                number_of_presents += (
                    house_number // elf_id
                    if house_number <= 50 * house_number // elf_id
                    else 0
                )

    return number_of_presents * 11


def solve(n_presents_target: int, compute_number_of_presents: Callable) -> int:
    n_presents = 0
    house_number = 0
    while n_presents < n_presents_target:
        house_number += 1
        n_presents = compute_number_of_presents(house_number)

    return house_number


if __name__ == "__main__":
    n_presents_target = 36000000
    print(
        f"Part 1:\nThe lowest house number that receives at least {n_presents_target} presents is {solve(n_presents_target, compute_number_of_presents_part1)}.\n"
    )
    print(
        f"Part 2:\nThe lowest house number that receives at least {n_presents_target} presents is {solve(n_presents_target, compute_number_of_presents_part2)}.\n"
    )
