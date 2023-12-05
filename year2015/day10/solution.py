"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say.
They take turns making sequences by reading aloud the previous sequence
and using that reading as the next sequence.
For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively,
using the previous value as input for the next step.
For each step, take the previous value,
and replace each run of digits (like 111) with the number of digits (3)
followed by the digit itself (1).

For example:

- `1` becomes `11` (1 copy of digit 1).
- `11` becomes `21` (2 copies of digit 1).
- `21` becomes `1211` (one 2 followed by one 1).
- `1211` becomes `111221` (one 1, one 2, and two 1s).
- `111221` becomes `312211` (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times.
What is the length of the result?

Your puzzle input is 1113222113.

--- Part Two ---

Neat, right? You might also enjoy hearing John Conway talking about this sequence
(that's Conway of Conway's Game of Life fame): https://youtu.be/ea7lJkEhytA.

Now, starting again with the digits in your puzzle input,
apply this process 50 times. What is the length of the new result?

--- Notes ---

- https://en.wikipedia.org/wiki/Look-and-say_sequence
- discovered `itertools.groupby` on https://www.reddit.com/r/adventofcode/comments/3w6h3m/day_10_solutions/

"""
from itertools import groupby


def play_look_and_say(sequence: str) -> str:

    final_sequence = ""
    for digit, digit_segment in groupby(sequence):
        final_sequence += f"{len(list(digit_segment))}{digit}"

    return final_sequence


# def play_look_and_say(sequence: str) -> str:

#     final_sequence = ""
#     current_digit = sequence[0]
#     current_digit_count = 0
#     for digit in sequence:
#         if digit == current_digit:
#             current_digit_count += 1
#             continue
#         final_sequence += f"{current_digit_count}{current_digit}"

#         current_digit = digit
#         current_digit_count = 1

#     final_sequence += f"{current_digit_count}{current_digit}"

#     return final_sequence


def solve(sequence: str, n_rounds: int) -> int:

    for _ in range(n_rounds):
        sequence = play_look_and_say(sequence)

    return len(sequence)


if __name__ == "__main__":

    print(
        f"Part 1:\nAfter 40 iterations, the length of the sequence is {solve('1113222113', 40)}.\n"
    )
    print(
        f"Part 2:\nAfter 50 iterations, the length of the sequence is {solve('1113222113', 50)}.\n"
    )
