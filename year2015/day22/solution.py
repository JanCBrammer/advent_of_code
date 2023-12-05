"""
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring.
Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns.
The player still goes first. Now, however, you don't get any equipment;
instead, you must choose one of your spells to cast.
The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally.
However, since you do magic damage, your opponent's armor is ignored,
and so the boss effectively has zero armor as well.
As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead -
that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast.
If you cannot afford to cast any spell, you lose.
Spells cost mana; you start with 500 mana, but have no maximum limit.
You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it.
Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

- Magic Missile costs 53 mana. It instantly does 4 damage.
- Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
- Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
- Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
- Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns.
Effects are created with a timer (the number of turns they last);
at the start of each turn, after they apply any effect they have, their timer is decreased by one.
If this decreases the timer to zero, the effect ends.
You cannot cast a spell that would start an effect which is already active.
However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

```
-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
```

Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

```
-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
```
You start with 50 hit points and 500 mana points.
The boss's actual stats are in your puzzle input.
What is the least amount of mana you can spend and still win the fight?
(Do not include mana recharge effects as "spending" negative mana.)

--- Part Two ---
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point.
If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss,
what is the least amount of mana you can spend and still win the fight?

--- Notes ---
https://en.wikipedia.org/wiki/Backtracking
https://christianjmills.com/posts/backtracking-notes/

Is BFS faster that DFS?

- Henry plays first.
- The first character at or below 0 hit points loses.
- If Henry's armor would reduce damage below 1, it becomes 1 instead - that is, the Boss' attacks always deal at least 1 damage.
- Casting a spell is mandatory on each of Henry's turns.
- If Henry cannot afford to cast any spell, he looses.
- Spell cost is immediately deducted when Henry casts it.
- Effects apply at the start of both Henry's turns and the Boss' turns.
- Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one.
- Effect end if timer is at zero.
- Henry cannot cast a spell that would start an effect which is already active.
- However, effects can be started on the same turn they end.

Note difference between spells that act instantly vs. those that act on the subsequent turn(s) once activated.

The correct answer for part 1 is 1269.
The correct answer for part 1 is 1309.
"""
import dataclasses
import copy
from typing import TypedDict, Iterator


@dataclasses.dataclass
class Player:
    hit_points: int = 0
    damage: int = 0
    armor: int = 0
    mana: int = 0


@dataclasses.dataclass
class Spell:
    name: str = ""
    cost: int = 0
    damage: int = 0
    armor: int = 0
    mana_gain: int = 0
    hit_point_gain: int = 0
    turns: int = 0

    def __eq__(self, other):
        return self.name == other.name


Game = TypedDict(
    "Game",
    {
        "Henry": Player,
        "Boss": Player,
        "multiturn_spells": list[Spell],
        "spell_history": list[Spell],
    },
)


@dataclasses.dataclass(eq=False)
class MagicMissile(Spell):
    name: str = "MagicMissile"
    cost: int = 53
    damage: int = 4


@dataclasses.dataclass(eq=False)
class Drain(Spell):
    name: str = "Drain"
    cost: int = 73
    damage: int = 2
    hit_point_gain: int = 2


@dataclasses.dataclass(eq=False)
class Shield(Spell):
    name: str = "Shield"
    cost: int = 113
    armor: int = 7
    turns: int = 6


@dataclasses.dataclass(eq=False)
class Poison(Spell):
    name: str = "Poison"
    cost: int = 173
    damage: int = 3
    turns: int = 6


@dataclasses.dataclass(eq=False)
class Recharge(Spell):
    name: str = "Recharge"
    cost: int = 229
    mana_gain: int = 101
    turns: int = 5


def cast_multiturn_spells(game: Game) -> Game:
    game["Henry"].armor = 0
    for spell in game["multiturn_spells"]:
        match spell:
            case Shield():
                game["Henry"].armor = spell.armor
            case Poison():
                game["Boss"].hit_points -= spell.damage
            case Recharge():
                game["Henry"].mana += spell.mana_gain
        spell.turns -= 1

    game["multiturn_spells"] = [
        spell for spell in game["multiturn_spells"] if spell.turns > 0
    ]

    return game


def get_winner(game: Game) -> str:
    if game["Boss"].hit_points <= 0:
        return "Henry"
    if game["Henry"].hit_points <= 0:
        return "Boss"

    return ""


def get_spell_candidates(game: Game) -> list[Spell]:
    mana_budget = game["Henry"].mana
    if Recharge() in game["multiturn_spells"]:
        # Recharge could increase Henry's mana before he casts the next spell
        mana_budget += Recharge().cost
    spells = [MagicMissile(), Drain(), Shield(), Poison(), Recharge()]
    multiturn_spells = [spell for spell in game["multiturn_spells"] if spell.turns > 1]
    affordable_spells = [spell for spell in spells if spell.cost <= mana_budget]
    valid_spells = [
        spell for spell in affordable_spells if spell not in multiturn_spells
    ]  # a spell can be cast on the same turn it ends

    return valid_spells


def play_two_turns(game: Game, spell: Spell, handicap_henry: int) -> Game:
    """Mutate game state according to spell."""
    game_copy = copy.deepcopy(game)

    # Henry's turn
    game_copy["Henry"].hit_points -= handicap_henry
    game_copy = cast_multiturn_spells(
        game_copy
    )  # Boss could die here; Henry's mana could increase

    game_copy["spell_history"].append(spell)
    game_copy["Henry"].mana -= spell.cost
    if spell.turns:
        # takes effect on subsequent turn(s)
        game_copy["multiturn_spells"].append(spell)
    else:
        # takes effect immediately
        game_copy["Boss"].hit_points -= spell.damage  # Boss could die here
        game_copy["Henry"].hit_points += spell.hit_point_gain

    # Boss's turn
    game_copy = cast_multiturn_spells(game_copy)  # Boss could die here

    game_copy["Henry"].hit_points -= max(
        game_copy["Boss"].damage - game_copy["Henry"].armor, 1
    )  # Henry could die here

    return game_copy


def play(game: Game, max_n_spells: int = 10, handicap_henry: int = 0) -> Iterator[int]:
    if len(game["spell_history"]) >= max_n_spells:
        return
    winner = get_winner(game)
    if winner == "Boss":
        return
    if winner == "Henry":
        yield sum(spell.cost for spell in game["spell_history"])
    for spell in get_spell_candidates(game):
        yield from play(
            play_two_turns(game, spell, handicap_henry), max_n_spells, handicap_henry
        )


def solve_part1():
    game: Game = {
        "Henry": Player(hit_points=50, mana=500),
        "Boss": Player(hit_points=58, damage=9),
        "multiturn_spells": [],
        "spell_history": [],
    }
    winning_budget = min(winning_budget for winning_budget in play(game))
    print(f"Part 1:\nHenry can win on a minimum budget of {winning_budget} mana.\n")


def solve_part2():
    game: Game = {
        "Henry": Player(hit_points=50, mana=500),
        "Boss": Player(hit_points=58, damage=9),
        "multiturn_spells": [],
        "spell_history": [],
    }
    winning_budget = min(
        winning_budget for winning_budget in play(game, handicap_henry=1)
    )
    print(
        f"Part 2:\nHandicapped Henry can win on a minimum budget of {winning_budget} mana.\n"
    )


if __name__ == "__main__":
    solve_part1()
    solve_part2()
