import pytest
from . import solution


@pytest.mark.parametrize(
    "house_number, n_presents",
    [
        (1, 10),
        (2, 30),
        (3, 40),
        (4, 70),
        (5, 60),
        (6, 120),
        (7, 80),
        (8, 150),
        (9, 130),
        (12, 280),
        (100000, 2460780),
    ],
)
def test_compute_number_of_presents(house_number: int, n_presents: int):
    assert solution.compute_number_of_presents_part1(house_number) == n_presents
