import pytest
from . import solution


@pytest.mark.parametrize(
    "coordinates, expected_code",
    [
        ((1, 1), 20151125),
        ((1, 6), 33511524),
        ((6, 1), 33071741),
        ((6, 6), 27995004),
    ],
)
def test_find_bar(coordinates: str, expected_code: int):
    assert solution.compute_code(*coordinates) == expected_code
