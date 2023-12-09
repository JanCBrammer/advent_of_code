import pytest
from . import solution


@pytest.fixture
def reindeer_performance_data():
    return {
        "Comet": {
            "go_distance_per_time": 14,
            "go_time": 10,
            "rest_time": 127,
        },
        "Dancer": {
            "go_distance_per_time": 16,
            "go_time": 11,
            "rest_time": 162,
        },
    }


@pytest.mark.parametrize(
    "reindeer, distance",
    [("Comet", 1120), ("Dancer", 1056)],
)
def test_compute_covered_distance(
    reindeer_performance_data: dict[str, dict[str, int]], reindeer: str, distance: int
):
    assert (
        solution.compute_covered_distance(1000, reindeer_performance_data[reindeer])
        == distance
    )


def test_compute_winning_points(reindeer_performance_data: dict[str, dict[str, int]]):
    assert solution.compute_winning_points(1000, reindeer_performance_data) == 689
