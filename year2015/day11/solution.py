"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires,
Santa has devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons),
so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers:
xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step;
if it was z, it wraps around to a,
and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started,
and he has imposed some additional password requirements:

- Passwords must include one increasing straight of at least three letters,
    like `abc`, `bcd`, `cde`, and so on, up to `xyz`.
    They cannot skip letters; `abd` doesn't count.
- Passwords may not contain the letters `i`, `o`, or `l`,
    as these letters can be mistaken for other characters and are therefore confusing.
- Passwords must contain at least two different, non-overlapping pairs of letters,
    like `aa`, `bb`, or `zz`.
For example:

- `hijklmmn` meets the first requirement (because it contains the straight `hij`)
    but fails the second requirement requirement (because it contains `i` and `l`).
- `abbceffg` meets the third requirement (because it repeats `bb` and `ff`)
    but fails the first requirement.
- `abbcegjk` fails the third requirement, because it only has one double letter (`bb`).
- The next password after `abcdefgh` is `abcdffaa`.
- The next password after `ghijklmn` is `ghjaabcc`,
    because you eventually skip all the passwords that start with `ghi`..., since `i` is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is `hepxcrrq`.

--- Part Two ---

Santa's password expired again. What's the next one?

--- Notes ---

"""
import re
from itertools import pairwise, groupby


def increment_password(password: str) -> str:
    """97 and 122 are Unicode characters 'a' and 'z'."""

    updated_password = ""
    updating = True

    for letter in password[::-1]:
        if updating:
            updated_password += chr(((ord(letter) + 1) - 97) % (122 - 97 + 1) + 97)
            updating = updated_password[-1] == "a"
            continue
        updated_password += letter

    return updated_password[::-1]


def password_is_valid(password: str) -> bool:

    if any(letter in password for letter in ["i", "o", "l"]):
        return False

    if len(set(re.findall(r"([a-z])\1{1,}", password))) < 2:
        return False

    alphabetic_diffs = [ord(j) - ord(i) for i, j, in pairwise(password)]
    if not 1 in alphabetic_diffs:
        return False
    if (
        max(
            len(list(diff_sequence))
            for diff, diff_sequence in groupby(alphabetic_diffs)
            if diff == 1
        )
        < 2
    ):
        return False

    return True


def solve(password: str) -> str:

    updated_password = increment_password(password)

    while not password_is_valid(updated_password):
        updated_password = increment_password(updated_password)

    return updated_password


if __name__ == "__main__":

    print(f"Part 1:\nSanta, your new password is {solve('hepxcrrq')}!\n")
    print(f"Part 2:\nSanta, your new password is {solve('hepxxyzz')}!\n")
