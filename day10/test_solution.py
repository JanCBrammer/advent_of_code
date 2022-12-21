import pytest
from . import solution


@pytest.mark.parametrize(
    "initial_sequence, final_sequence",
    [
        ("1", "11"),
        ("11", "21"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test_look_and_say(initial_sequence: str, final_sequence: str):

    assert solution.play_look_and_say(initial_sequence) == final_sequence
