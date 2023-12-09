import pytest
from . import solution


@pytest.fixture
def happiness_changes():
    return {
        "Alice": {"Bob": 54, "Carol": -79, "David": -2},
        "Bob": {"Alice": 83, "Carol": -7, "David": -63},
        "Carol": {"Alice": -62, "Bob": 60, "David": 55},
        "David": {"Alice": 46, "Bob": -7, "Carol": 41},
    }


@pytest.mark.parametrize(
    "seating_arrangement, happiness_change",
    [
        (("David", "Alice", "Bob", "Carol"), 330),
    ],
)
def test_compute_happiness(
    seating_arrangement: tuple[str],
    happiness_changes: dict[str, dict[str, int]],
    happiness_change: int,
):
    assert (
        solution.compute_happiness(seating_arrangement, happiness_changes)
        == happiness_change
    )


def test_find_optimal_seating_arrangement(happiness_changes: dict[str, dict[str, int]]):
    assert solution.find_optimal_seating_arrangement(happiness_changes) == 330
