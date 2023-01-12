"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients.
You make a list of the remaining ingredients you could use to finish the recipe
(your puzzle input) and their properties per teaspoon:

- `capacity` (how well it helps the cookie absorb milk)
- `durability` (how well it keeps the cookie intact when full of milk)
- `flavor` (how tasty it makes the cookie)
- `texture` (how it improves the feel of the cookie)
- `calories` (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the future.
The total score of a cookie can be found by adding up each of the properties
(negative totals become 0) and then multiplying together everything except
calories.

For instance, suppose you have these two ingredients:

```
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
```
Then, choosing to use 44 teaspoons of butterscotch and
56 teaspoons of cinnamon (because the amounts of each ingredient
must add up to 100) would result in a cookie with the following properties:

- `capacity` of `44*-1 + 56*2 = 68`
- `durability` of `44*-2 + 56*3 = 80`
- `flavor` of `44*6 + 56*-2 = 152`
- `texture` of `44*3 + 56*-1 = 76`

Multiplying these together (`68 * 80 * 152 * 76`, ignoring calories for now)
results in a total score of 62842880,
which happens to be the best score possible given these ingredients.
If any properties had produced a negative total,
it would have instead become zero,
causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties,
what is the total score of the highest-scoring cookie you can make?

--- Part Two ---

Your cookie recipe becomes wildly popular!
Someone asks if you can make another recipe that has exactly 500 calories per cookie
(so they can use it as a meal replacement).
Keep the rest of your award-winning process the same
(100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected
40 teaspoons of butterscotch and 60 teaspoons of cinnamon
(which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500.
The total score would go down, though: only 57600000,
the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties,
what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

--- Notes ---

- does every ingredient have to be used?
- no approximation
- no non-integer solutions, i.e., no constrained optimization
- the number of teaspoons per ingredient must be the same across all properties
- generate all k-compositions for 100 tablespoons, and find the optimal k-composition (that maximizes the score)
    - a k-composition, is a way to write an integer (100 tablespoons)
      as the sum of an ordered sequence of positive integers (number of tablespoons per ingredient):
      https://en.wikipedia.org/wiki/Composition_(combinatorics)
    - not to be confused with integer partition, where order doesn't matter
    - if not all ingredients need to be used, find the optimal "weak k-composition"
    - https://stackoverflow.com/questions/15577651/generate-all-compositions-of-an-integer-into-k-parts
    - https://stackoverflow.com/questions/4647120/next-composition-of-n-into-k-parts-does-anyone-have-a-working-algorithm?noredirect=1&lq=1
"""
from pathlib import Path
from itertools import starmap
from operator import mul
from math import prod
from typing import Callable
import re


def parse_input(input_path: str) -> list[tuple[int, ...]]:

    ingredients = []
    with Path(input_path).open() as file:
        for line in file:
            ingredients.append(tuple(int(i) for i in re.findall(r"-?\d+", line)))

    return list(zip(*ingredients))


def compose_teaspoons(n_ingredients: int, n_tablespoons: int, parent=tuple()):
    if n_ingredients > 1:
        for n in range(n_tablespoons + 1):
            for composition in compose_teaspoons(
                n_ingredients - 1, n, parent + (n_tablespoons - n,)
            ):
                yield composition
    else:
        yield parent + (n_tablespoons,)


def compute_cookie_property_score(
    composition: tuple[int, ...], properties: tuple[int, ...]
) -> int:

    property_score = sum(list(starmap(mul, list(zip(composition, properties)))))

    return max(property_score, 0)


def compute_cookie_score(
    composition: tuple[int, ...], ingredient_properties: list[tuple[int, ...]]
) -> int:

    return prod(
        [
            compute_cookie_property_score(composition, property)
            for property in ingredient_properties[:-1]
        ]
    )


def compute_cookie_score_with_calorie_constraint(
    composition: tuple[int, ...], ingredient_properties: list[tuple[int, ...]]
) -> int:

    cookie_score = 0

    property_scores = [
        compute_cookie_property_score(composition, property)
        for property in ingredient_properties
    ]

    if property_scores[-1] == 500:
        cookie_score = prod(property_scores[:-1])

    return cookie_score


def find_max_cookie_score(
    ingredient_properties: list[tuple[int, ...]],
    n_ingredients: int,
    n_tablespoons: int,
    cookie_scorer: Callable,
) -> int:
    max_cookie_score = 0

    for composition in compose_teaspoons(n_ingredients, n_tablespoons):
        cookie_score = cookie_scorer(composition, ingredient_properties)
        max_cookie_score = max(cookie_score, max_cookie_score)

    return max_cookie_score


def solve(input_path: str):

    ingredient_properties = parse_input(input_path)

    max_cookie_score_part1 = find_max_cookie_score(
        ingredient_properties, 4, 100, compute_cookie_score
    )
    print(f"Part 1:\nThe highest possible cookie score is {max_cookie_score_part1}.\n")

    max_cookie_score_part2 = find_max_cookie_score(
        ingredient_properties, 4, 100, compute_cookie_score_with_calorie_constraint
    )
    print(
        f"Part 2:\nThe highest possible score for a cookie with 500 calories is {max_cookie_score_part2}.\n"
    )


if __name__ == "__main__":

    solve(f"{Path(__file__).parts[-2]}/input.txt")
