"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!
Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
A signal is provided to each wire by a gate, another wire, or some specific value.
Each wire can only get a signal from one source, but can provide its signal to multiple destinations.
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
`x AND y -> z` means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

- `123 -> x` means that the signal 123 is provided to wire x.
- `x AND y -> z` means that the bitwise AND of wire x and wire y is provided to wire z.
- `p LSHIFT 2 -> q` means that the value from wire p is left-shifted by 2 and then provided to wire q.
- `NOT e -> f` means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
If, for some reason, you'd like to emulate the circuit instead,
almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```
After it is run, these are the signals on the wires:
```
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal,
and reset the other wires (including wire a).
What new signal is ultimately provided to wire a?

--- Notes ---

- https://realpython.com/python-bitwise-operators/
- https://wiki.python.org/moin/BitwiseOperators
- https://en.wikipedia.org/wiki/Bitwise_operation
- https://en.wikipedia.org/wiki/16-bit_computing
- https://en.wikipedia.org/wiki/Logical_shift
- https://gist.github.com/coolharsh55/711360947b40e8cc404e
"""
from pathlib import Path
from operator import and_, or_, invert, lshift, rshift
from collections import namedtuple

Operation = namedtuple("Operation", "operands operator")


def parse_input(input_path: str) -> str:
    circuit = {}
    with Path(input_path).open() as file:
        for instruction in file:
            operation, wire = instruction.split("->")
            circuit[wire.strip()] = parse_operation(operation)

    return circuit


def parse_operation(operation: str) -> namedtuple:
    if "AND" in operation:
        operands = [operand.strip() for operand in operation.split("AND")]
        operator = and_

    elif "OR" in operation:
        operands = [operand.strip() for operand in operation.split("OR")]
        operator = or_

    elif "LSHIFT" in operation:
        operands = [operand.strip() for operand in operation.split("LSHIFT")]
        operator = lshift

    elif "RSHIFT" in operation:
        operands = [operand.strip() for operand in operation.split("RSHIFT")]
        operator = rshift

    elif "NOT" in operation:
        operands = [operation.removeprefix("NOT").strip()]
        operator = invert

    else:
        operands = [operation.strip()]
        operator = None

    typed_operands = [
        int(operand) if operand.isdigit() else operand for operand in operands
    ]

    if len(typed_operands) == 1 and isinstance(typed_operands[0], int):
        return typed_operands[0]

    return Operation(typed_operands, operator)


def compute_wire_input(wire: str, circuit: dict) -> int:
    wires_to_compute = [wire]

    while wires_to_compute:
        current_wire = wires_to_compute.pop()
        wire_input = circuit[current_wire]

        if isinstance(wire_input, int):
            continue

        if wire_input.operator is None:
            circuit[current_wire] = circuit[wire_input.operands[0]]

        computable = all(
            isinstance(operand, int) or isinstance(circuit[operand], int)
            for operand in wire_input.operands
        )

        if computable:
            circuit[current_wire] = wire_input.operator(
                *[
                    circuit[operand] if isinstance(operand, str) else operand
                    for operand in wire_input.operands
                ]
            )
        else:
            wires_to_compute.append(current_wire)
            wires_to_compute.extend(
                [operand for operand in wire_input.operands if isinstance(operand, str)]
            )

    return circuit[wire]


def solve(input_path: str):
    circuit = parse_input(input_path)

    return compute_wire_input("a", circuit)


if __name__ == "__main__":
    input_dir = Path(__file__).parent
    input_path_part1 = f"{input_dir}/input_part1.txt"
    input_path_part2 = f"{input_dir}/input_part2.txt"

    print(f"Part 1:\nWire 'a' receives input {solve(input_path_part1)}.\n")
    print(f"Part 2:\nWire 'a' receives input {solve(input_path_part2)}.\n")
