import pytest
from . import solution


@pytest.mark.parametrize(
    "directions, visited_houses",
    [
        (">", {(0, 0), (1, 0)}),
        ("^>v<", {(0, 0), (0, 1), (1, 1), (1, 0)}),
        ("^v^v^v^v^v", {(0, 0), (0, 1)}),
    ],
)
def test_track_visited_houses(directions: str, visited_houses: set[tuple[int, int]]):

    assert solution.track_visited_houses(directions) == visited_houses


@pytest.mark.parametrize(
    "directions, visited_houses",
    [
        ("^v", {(0, -1), (0, 0), (0, 1)}),
        ("^>v<", {(0, 0), (0, 1), (1, 0)}),
        (
            "^v^v^v^v^v",
            {
                (0, 1),
                (0, -3),
                (0, 4),
                (0, 0),
                (0, 3),
                (0, -2),
                (0, -4),
                (0, 2),
                (0, 5),
                (0, -5),
                (0, -1),
            },
        ),
    ],
)
def test_track_visited_houses_robosanta(
    directions: str, visited_houses: set[tuple[int, int]]
):

    assert solution.track_visited_houses_robosanta(directions) == visited_houses
