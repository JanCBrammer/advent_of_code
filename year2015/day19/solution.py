"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine.
Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant,
capable of constructing any Red-Nosed Reindeer molecule you need.
It works by starting with some input molecule and then doing a series of replacements,
one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used.
Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

```
H => HO
H => OH
O => HH
```
Given the replacements above and starting with `HOH,` the following molecules could be generated:

```
- HOOH (via H => HO on the first H).
- HOHO (via H => HO on the second H).
- OHOH (via H => OH on the first H).
- HOOH (via H => OH on the second H).
- HHHH (via O => HH).
```
So, in the example above, there are 4 distinct molecules (not five, because `HOOH` appears twice) after one replacement from `HOH`.
Santa's favorite molecule, `HOHOHO`, can become 7 distinct molecules (over nine replacements: six from `H`, and three from `O`).

The machine replaces without regard for the surrounding characters.
For example, given the string `H2O`, the transition `H` => `OO` would result in `OO2O`.

Your puzzle input describes all of the possible replacements and, at the bottom,
the medicine molecule for which you need to calibrate the machine.
How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

--- Part Two ---

Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e,
and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

```
e => H
e => O
H => HO
H => OH
O => HH
```
If you'd like to make HOH, you start with e, and then make the following replacements:

- `e` => `O` to get `O`
- `O` => `HH` to get `HH`
- `H` => `OH` (on the second `H`) to get `HOH`

So, you could make `HOH` after 3 steps.
Santa's favorite molecule, `HOHOHO`, can be made in 6 steps.

How long will it take to make the medicine?
Given the available replacements and the medicine molecule in your puzzle input,
what is the fewest number of steps to go from `e` to the medicine molecule?

--- Notes ---

Order of patterns to match is crucial:

    >>> import re

    >>> patterns = ["H", "O", "HH"]
    >>> target = "HHHOO"

    >>> list(re.finditer(re.compile("|".join(patterns)), target))
    [<re.Match object; span=(0, 1), match='H'>, <re.Match object; span=(1, 2), match='H'>, <re.Match object; span=(2, 3), match='H'>, <re.Match object; span=(3, 4), match='O'>, <re.Match object; span=(4, 5), match='O'>]

    "HH" isn't matched :(
        
    >>> patterns = sorted(patterns, reverse=True, key=len)
    >>> patterns
    ['HH', 'H', 'O']
    >>> list(re.finditer(re.compile("|".join(patterns)), target))
    [<re.Match object; span=(0, 2), match='HH'>, <re.Match object; span=(2, 3), match='H'>, <re.Match object; span=(3, 4), match='O'>, <re.Match object; span=(4, 5), match='O'>]

    Now "HH" is matched :)
"""
import re
import random
from pathlib import Path
from collections import defaultdict
from typing import Iterator
import bisect


def parse_input_part1(input_path: str) -> tuple[dict[str, set[str]], str]:
    replacements: dict = defaultdict(set)

    with Path(input_path).open() as file:
        for line in file:
            if "=>" in line:
                element, replacement = line.split("=>")
                replacements[element.strip()].add(replacement.strip())

        molecule = line.strip()

    return replacements, molecule


def parse_input_part2(input_path: str) -> tuple[dict[str, str], str]:
    replacements: dict = {}

    with Path(input_path).open() as file:
        for line in file:
            if "=>" in line:
                element, replacement = line.split("=>")
                replacements[replacement.strip()] = element.strip()

        molecule = line.strip()

    return replacements, molecule


def find_molecule_children(
    element_replacements: dict[str, set[str]], molecule: str
) -> Iterator[str]:
    for match in re.finditer(re.compile("|".join(element_replacements)), molecule):
        for replacement in element_replacements[match.group()]:
            yield f"{molecule[: match.start()]}{replacement}{molecule[match.end() :]}"


def find_molecule_parents(
    element_replacements: dict[str, str], molecule: str
) -> Iterator[str]:
    for element, replacement in element_replacements.items():
        for match in re.finditer(element, molecule):
            yield f"{molecule[: match.start()]}{replacement}{molecule[match.end() :]}"


def revert_molecule(
    element_replacements: dict[str, str],
    start_molecule: str,
) -> int:
    molequeue = [(start_molecule, 0)]
    explored_molecules = set()
    n_runs = 0

    while molequeue:
        if not (
            n_runs % 200
        ):  # 200 determined empirically, seems to result in quicker convergence than 100
            random.shuffle(molequeue)  # get unstuck from local extrema

        molecule, depth = molequeue.pop()
        n_runs += 1

        if molecule == "e":
            break

        if molecule in explored_molecules:
            continue
        explored_molecules.add(molecule)

        for parent_molecule in find_molecule_parents(element_replacements, molecule):
            molequeue.append((parent_molecule, depth + 1))
            bisect.insort_left(
                molequeue, (parent_molecule, depth + 1), key=lambda x: len(x[0])
            )  # try shorter candidates first

    return depth


def solve_part1(input_path: str):
    element_replacements, molecule = parse_input_part1(input_path)
    child_molecules = set(find_molecule_children(element_replacements, molecule))

    print(
        f"Part 1:\nA total of {len(child_molecules)} distinct molecules can be created.\n"
    )


def solve_part2(input_path: str):
    element_replacements, molecule = parse_input_part2(input_path)

    print(
        "Part 2:\nThe minimum number of steps to produce the medicine molecule is"
        f" {revert_molecule(element_replacements, molecule.strip())}.\n"
    )


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
