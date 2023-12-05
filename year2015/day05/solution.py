"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

- ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
- aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
- jchzalrnumimnmhp is naughty because it has no double letter.
- haegwjzuvuyypxyu is naughty because it contains the string xy.
- dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice.
None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

- It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
- It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

- qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
- xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
- uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
- ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

--- Notes ---

Interactive RegEx playground for Python: https://pythex.org

"""
from pathlib import Path
from typing import Callable, Iterator
import re


def string_contains_repeated_letter(string: str) -> bool:
    match = re.compile(r"([a-z])\1{1,}").search(string)
    if not match:
        return False
    return True


def string_contains_vowels(string: str) -> bool:
    match = re.findall("[aeiou]", string)
    if len(match) < 3:
        return False
    return True


def string_free_of_forbidden_substrings(string: str) -> bool:
    match = [substring in string for substring in ["ab", "cd", "pq", "xy"]]
    if any(match):
        return False
    return True


def string_contains_repeated_letter_pair(string: str) -> bool:
    match = re.compile(r"([a-z]{2})[a-z]*\1").search(string)
    if not match:
        return False
    return True


def string_contains_separated_repeated_letter(string: str) -> bool:
    match = re.compile(r"([a-z]{1})[a-z]{1}\1").search(string)
    if not match:
        return False
    return True


RULES_PART1 = (
    string_contains_repeated_letter,
    string_contains_vowels,
    string_free_of_forbidden_substrings,
)

RULES_PART2 = (
    string_contains_repeated_letter_pair,
    string_contains_separated_repeated_letter,
)


def string_is_nice(string: str, rules: tuple[Callable[[str], bool], ...]) -> bool:
    if all(rule(string) for rule in rules):
        return True

    return False


def parse_input(input_path: str) -> Iterator[str]:
    with Path(input_path).open() as file:
        for line in file:
            yield line


def count_nice_strings(
    input_path: str,
    rules: tuple[Callable[[str], bool], ...],
) -> int:
    n_nice_strings = 0
    for line in parse_input(input_path):
        if string_is_nice(line, rules):
            n_nice_strings += 1

    return n_nice_strings


if __name__ == "__main__":
    input_path = f"{Path(__file__).parent}/input.txt"

    print(
        f"Part 1:\nSanta, {count_nice_strings(input_path, RULES_PART1)} strings are nice!\n"
    )
    print(
        f"Part 2:\nSanta, {count_nice_strings(input_path, RULES_PART2)} strings are nice!\n"
    )
