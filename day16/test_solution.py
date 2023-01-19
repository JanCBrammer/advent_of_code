import pytest
from . import solution


@pytest.mark.parametrize(
    "aunt_attributes, match",
    [
        ({"vizslas": 0, "akitas": 1, "perfumes": 2}, False),
        ({"cats": 7, "pomeranians": 3, "goldfish": 5}, False),
        ({"cats": 8, "pomeranians": 2, "goldfish": 4}, True),
    ],
)
def test_match_aunt(aunt_attributes: dict[str, int], match: bool):

    assert solution.match_aunt(aunt_attributes) == match
