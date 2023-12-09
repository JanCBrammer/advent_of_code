import pytest
import struct
from operator import and_, or_, invert, lshift, rshift
from . import solution


@pytest.mark.parametrize(
    "operation, parsed_operation",
    [
        ("x AND y", solution.Operation(["x", "y"], and_)),
        ("1 AND y", solution.Operation([1, "y"], and_)),
        ("x OR y", solution.Operation(["x", "y"], or_)),
        ("x LSHIFT 2", solution.Operation(["x", 2], lshift)),
        ("y RSHIFT 2", solution.Operation(["y", 2], rshift)),
        ("NOT x", solution.Operation(["x"], invert)),
        ("x", solution.Operation(["x"], None)),
        ("123", 123),
    ],
)
def test_parse_operation(operation: str, parsed_operation: dict[dict]):
    assert solution.parse_operation(operation) == parsed_operation


@pytest.mark.parametrize(
    "operands, operator, result",
    [
        ((123, 456), and_, 72),
        ((123, 456), or_, 507),
        ((123, 2), lshift, 492),
        ((456, 2), rshift, 114),
        (tuple([123]), invert, struct.unpack("h", struct.pack("H", 65412))[0]),
        (tuple([456]), invert, struct.unpack("h", struct.pack("H", 65079))[0]),
        ((72, 65412), and_, 0),
        ((72, 114), or_, 122),
    ],
)
def test_compute_operation(operands: tuple[int], operator: callable, result: int):
    assert operator(*operands) == result


@pytest.fixture
def circuit():
    return {
        "d": solution.Operation(["x", "y"], and_),
        "e": solution.Operation(["x", "y"], or_),
        "f": solution.Operation(["x", 2], lshift),
        "g": solution.Operation(["y", 2], rshift),
        "h": solution.Operation(["x"], invert),
        "i": solution.Operation(["y"], invert),
        "j": solution.Operation(["d", "h"], and_),
        "k": solution.Operation(["d", "g"], or_),
        "l": solution.Operation(["j"], None),
        "x": 123,
        "y": 456,
    }


@pytest.mark.parametrize(
    "wire, result",
    [
        ("x", 123),
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", -124),
        ("i", -457),
        ("j", 0),
        ("k", 122),
        ("l", 0),
    ],
)
def test_compute_wire_input(circuit, wire, result):
    assert solution.compute_wire_input(wire, circuit) == result
