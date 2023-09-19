"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor.
It comes with instructions and an example program, but the computer itself seems to be malfunctioning.
She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions
(truly, it goes on to remind the reader, a state-of-the-art technology).
The registers are named `a` and `b`, can hold any non-negative integer,
and begin with a value of `0`. The instructions are as follows:

- `hlf r` sets register `r` to half its current value, then continues with the next instruction.
- `tpl r` sets register `r` to triple its current value, then continues with the next instruction.
- `inc r` increments register `r`, adding `1` to it, then continues with the next instruction.
- `jmp offset` is a jump; it continues with the instruction `offset` away relative to itself.
- `jie r, offset` is like `jmp`, but only jumps if register `r` is even ("jump if even").
- `jio r, offset` is like `jmp`, but only jumps if register `r` is `1` ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction.
The offset is always written with a prefix `+` or `-` to indicate the direction of the jump
(forward or backward, respectively).
For example, `jmp +1` would simply continue with the next instruction,
while `jmp +0` would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets `a` to `2`, because the `jio` instruction causes it
to skip the `tpl` instruction:

```
inc a
jio a, +2
tpl a
inc a
```

What is the value in register `b` when the program in your puzzle input is finished executing?

--- Part Two ---

The unknown benefactor is very thankful for releasi-- er,
helping little Jane Marie with her computer.
Definitely not to distract you, what is the value in register `b`
after the program is finished executing if register `a` starts as `1` instead?

--- Notes ---

Datastructure that holds the instructions needs to be index-able (for jumping).
At which instruction does the program start?
Which instruction is executed if conditional jump doesn't fire?
Is the default offset 1?
"""
from pathlib import Path
from typing import Final

PROGRAM: Final[list[str]] = (
    Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
)


def run_program(program: list[str], registers: dict[str, int]) -> dict[str, int]:
    instruction_index = 0

    while (instruction_index >= 0) and (instruction_index < len(program)):
        instruction_parts = program[instruction_index].split(" ")
        instruction = instruction_parts[0]
        offset_sign = ""
        instruction_index_offset = 1

        match instruction:
            case "hlf":
                registers[instruction_parts[1]] //= 2
            case "tpl":
                registers[instruction_parts[1]] *= 3
            case "inc":
                registers[instruction_parts[1]] += 1
            case "jmp":
                offset_sign = instruction_parts[1][0]
                instruction_index_offset = int(instruction_parts[1][1:])
            case "jie":
                if registers[instruction_parts[1].strip(",")] % 2 == 0:
                    offset_sign = instruction_parts[2][0]
                    instruction_index_offset = int(instruction_parts[2][1:])
            case "jio":
                if registers[instruction_parts[1].strip(",")] == 1:
                    offset_sign = instruction_parts[2][0]
                    instruction_index_offset = int(instruction_parts[2][1:])
            case _:
                print(f"Unknown instruction: {instruction}")

        if offset_sign == "-":
            instruction_index_offset *= -1

        instruction_index += instruction_index_offset

    return registers


def solve_part1():
    initial_registers: dict[str, int] = {"a": 0, "b": 0}
    final_registers = run_program(PROGRAM, initial_registers)

    print(
        f"Part 1:\nAfter running the program, register 'b' has the value {final_registers['b']}\n"
    )


def solve_part2():
    initial_registers: dict[str, int] = {"a": 1, "b": 0}
    final_registers = run_program(PROGRAM, initial_registers)

    print(
        f"Part 2:\nAfter running the program, register 'b' has the value {final_registers['b']}\n"
    )


if __name__ == "__main__":
    solve_part1()
    solve_part2()
