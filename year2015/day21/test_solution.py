import pytest
from . import solution


@pytest.fixture
def henry():
    return solution.Henry(hit_points=8, damage=5, armor=5)


@pytest.fixture
def boss():
    return solution.Boss(hit_points=12, damage=7, armor=2)


def test_compute_winner(henry, boss):
    assert solution.compute_winner(henry, boss).name == "Henry"
