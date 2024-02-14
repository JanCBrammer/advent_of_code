import pytest
from . import solution


@pytest.mark.parametrize(
    "shift, screen, expected",
    [
        (
            1,
            [[True, False, True, False, False, False, False]],
            [[False, True, False, True, False, False, False]],
        ),
        (
            5,
            [[True, False, True, False, False, False, False]],
            [[True, False, False, False, False, True, False]],
        ),
        (
            7,
            [[True, False, True, False, False, False, False]],
            [[True, False, True, False, False, False, False]],
        ),
        (
            8,
            [[True, False, True, False, False, False, False]],
            [[False, True, False, True, False, False, False]],
        ),
    ],
)
def test_rotate_row(shift: int, screen: list[list[bool]], expected: list[list[bool]]):
    assert solution.rotate_row(0, shift, screen) == expected


@pytest.mark.parametrize(
    "shift, screen, expected",
    [
        (
            1,
            [[True], [False], [True], [False], [False], [False], [False]],
            [[False], [True], [False], [True], [False], [False], [False]],
        ),
        (
            5,
            [[True], [False], [True], [False], [False], [False], [False]],
            [[True], [False], [False], [False], [False], [True], [False]],
        ),
        (
            7,
            [[True], [False], [True], [False], [False], [False], [False]],
            [[True], [False], [True], [False], [False], [False], [False]],
        ),
        (
            8,
            [[True], [False], [True], [False], [False], [False], [False]],
            [[False], [True], [False], [True], [False], [False], [False]],
        ),
    ],
)
def test_rotate_column(
    shift: int, screen: list[list[bool]], expected: list[list[bool]]
):
    assert solution.rotate_column(0, shift, screen) == expected
