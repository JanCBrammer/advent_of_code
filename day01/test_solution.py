import pytest
from . import solution


@pytest.mark.parametrize(
    "directions, floor",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_find_floor(directions: str, floor: int):

    assert solution.find_floor(directions) == floor


@pytest.mark.parametrize(
    "directions, position",
    [(")", 1), ("()())", 5)],
)
def test_find_basement_entrance_direction(directions: str, position: int):

    assert solution.find_basement_entrance_direction(directions) == position
