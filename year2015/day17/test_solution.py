import pytest
from . import solution


@pytest.mark.parametrize(
    "containers, container_combinations",
    [
        ((20, 15, 10, 5, 5), [(20, 5), (20, 5), (15, 10), (15, 5, 5)]),
    ],
)
def test_find_container_combinations(
    containers: tuple[int, ...], container_combinations: list[tuple[int, ...]]
):

    assert (
        solution.find_container_combinations(containers, 25) == container_combinations
    )
