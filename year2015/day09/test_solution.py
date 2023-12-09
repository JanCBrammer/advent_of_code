import pytest
from . import solution


@pytest.fixture
def city_distances():
    return {
        "London": {"Dublin": 464, "Belfast": 518},
        "Dublin": {"London": 464, "Belfast": 141},
        "Belfast": {"London": 518, "Dublin": 141},
    }


@pytest.mark.parametrize(
    "cities, path_length",
    [
        (["London", "Dublin", "Belfast"], 605),
        (["Dublin", "London", "Belfast"], 982),
        (["London", "Belfast", "Dublin"], 659),
    ],
)
def test_compute_path_length(
    cities: list[str], path_length: int, city_distances: dict[str, dict[str, int]]
):
    assert solution.compute_path_length(cities, city_distances) == path_length


def test_find_shortest_path(city_distances: dict[str, dict[str, int]]):
    assert solution.find_extreme_path(city_distances, float("inf"), min) == 605


def test_find_longest_path(city_distances: dict[str, dict[str, int]]):
    assert solution.find_extreme_path(city_distances, float("0"), max) == 982
