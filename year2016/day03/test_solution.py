from . import solution


def test_triangle_is_valid():
    assert not solution.triangle_is_valid((5, 10, 25))
