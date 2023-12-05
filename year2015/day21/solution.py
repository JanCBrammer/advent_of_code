"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas.
It's an RPG, and he's stuck on a boss.
He needs to know what equipment to buy at the shop.
He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking.
The player always goes first. Each attack reduces the opponent's hit points by at least `1`.
The first character at or below `0` hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.
An attacker always does at least `1` damage.
So, if the attacker has a damage score of `8`, and the defender has an armor score of `3`,
the defender loses `5` hit points.
If the defender had an armor score of `300`, the defender would still lose `1` hit point.

Your damage score and armor score both start at zero.
They can be increased by buying items in exchange for gold.
You start with no items and have as much gold as you need.
Your total damage or armor is equal to the sum of those stats from all of your items.
You have `100` hit points.

Here is what the item shop is selling:

```
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
```

You must buy exactly one weapon; no dual-wielding.
Armor is optional, but you can't use more than one.
You can buy 0-2 rings (at most one for each hand).
You must use any items you buy.
The shop only has one of each item, so you can't buy,
for example, two rings of Damage +3.

For example, suppose you have `8` hit points, `5` damage, and `5` armor,
and that the boss has `12` hit points, `7` damage, and `2` armor:

- The player deals `5-2 = 3` damage; the boss goes down to `9` hit points.
- The boss deals `7-5 = 2` damage; the player goes down to `6` hit points.

- The player deals `5-2 = 3` damage; the boss goes down to `6` hit points.
- The boss deals `7-5 = 2` damage; the player goes down to `4` hit points.

- The player deals `5-2 = 3` damage; the boss goes down to `3` hit points.
- The boss deals `7-5 = 2` damage; the player goes down to `2` hit points.

- The player deals `5-2 = 3` damage; the boss goes down to `0` hit points.

In this scenario, the player wins! (Barely.)

You have `100` hit points. The boss's actual stats are in your puzzle input.
What is the least amount of gold you can spend and still win the fight?

--- Part Two ---
Turns out the shopkeeper is working with the boss,
and can persuade you to buy whatever items he wants.
The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

--- Notes ---

"""
from dataclasses import dataclass
from itertools import combinations, product
from functools import reduce
from operator import add
from typing import Final, Union


@dataclass
class Henry:
    name: str = "Henry"
    hit_points: int = 100
    damage: int = 0
    armor: int = 0


@dataclass
class Boss:
    name: str = "Boss"
    hit_points: int = 104
    damage: int = 8
    armor: int = 1


@dataclass
class Item:
    cost: int = 0
    damage: int = 0
    armor: int = 0

    def __add__(self, other):
        return Item(
            cost=self.cost + other.cost,
            damage=self.damage + other.damage,
            armor=self.armor + other.armor,
        )


WEAPONS: Final[tuple[Item, ...]] = (
    Item(cost=8, damage=4, armor=0),
    Item(cost=10, damage=5, armor=0),
    Item(cost=25, damage=6, armor=0),
    Item(cost=40, damage=7, armor=0),
    Item(cost=74, damage=8, armor=0),
)

ARMOR: Final[tuple[Item, ...]] = (
    Item(),
    Item(cost=13, damage=0, armor=1),
    Item(cost=31, damage=0, armor=2),
    Item(cost=53, damage=0, armor=3),
    Item(cost=75, damage=0, armor=4),
    Item(cost=102, damage=0, armor=5),
)

RINGS: Final[tuple[Item, ...]] = (
    Item(cost=20, damage=0, armor=1),
    Item(cost=25, damage=1, armor=0),
    Item(cost=40, damage=0, armor=2),
    Item(cost=50, damage=2, armor=0),
    Item(cost=80, damage=0, armor=3),
    Item(cost=100, damage=3, armor=0),
)


def get_ring_combinations() -> list[Item]:
    ring_pair_sums = [reduce(add, c) for c in combinations(RINGS, 2)]

    return sorted([Item(), *RINGS, *ring_pair_sums], key=lambda item: item.cost)


def get_item_combinations() -> list[Item]:
    item_combinations = product(WEAPONS, ARMOR, get_ring_combinations())
    item_combination_sums = [reduce(add, c) for c in item_combinations]

    return sorted(item_combination_sums, key=lambda item: item.cost)


def compute_winner(henry: Henry, boss: Boss) -> Union[Henry, Boss]:
    while True:
        boss.hit_points -= max((henry.damage - boss.armor), 1)
        if boss.hit_points <= 0:
            return henry

        henry.hit_points -= max((boss.damage - henry.armor), 1)
        if henry.hit_points <= 0:
            return boss


def solve_part1():
    for item_combination in get_item_combinations():
        if (
            compute_winner(
                Henry(damage=item_combination.damage, armor=item_combination.armor),
                Boss(),
            ).name
            == "Henry"
        ):
            break

    print(
        f"Part 1:\nHenry can win the fight on a minimum budget of {item_combination.cost} gold.\n"
    )


def solve_part2():
    for item_combination in reversed(get_item_combinations()):
        if (
            compute_winner(
                Henry(damage=item_combination.damage, armor=item_combination.armor),
                Boss(),
            ).name
            == "Boss"
        ):
            break

    print(
        f"Part 2:\nHenry can loose the fight on a maximum budget of {item_combination.cost} gold.\n"
    )


if __name__ == "__main__":
    solve_part1()
    solve_part2()
