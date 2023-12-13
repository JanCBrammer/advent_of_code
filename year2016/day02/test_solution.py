import pytest
from . import solution


@pytest.mark.parametrize(
    "keypad, initial_button_coordinates, expected_bathroom_code",
    [
        (solution.KEYPAD_PART1, (2, 2), "1985"),
        (solution.KEYPAD_PART2, (1, 3), "5DB3"),
    ],
)
def test_find_bathroom_code(keypad, initial_button_coordinates, expected_bathroom_code):
    instructions = [
        "ULL",
        "RRDDD",
        "LURDL",
        "UUUUD",
    ]

    assert (
        solution.find_bathroom_code(instructions, keypad, *initial_button_coordinates)
        == expected_bathroom_code
    )
