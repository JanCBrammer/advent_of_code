import pytest
from . import solution


@pytest.fixture
def light_grid_all_off():
    return [[False, False, False], [False, False, False], [False, False, False]]


@pytest.fixture
def light_grid_all_on():
    return [[True, True, True], [True, True, True], [True, True, True]]


@pytest.fixture
def light_grid_partly_on():
    return [[True, True, True], [True, True, False], [True, True, False]]


@pytest.fixture
def light_grid_varying_brightness():
    return [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def test_turn_lights_on(light_grid_all_off):
    mode = "on"
    coordinates = ((1, 0), (2, 1))

    assert solution.change_light_state(mode, coordinates, light_grid_all_off) == [
        [False, False, False],
        [True, True, False],
        [True, True, False],
    ]


def test_turn_lights_off(light_grid_all_on):
    mode = "off"
    coordinates = ((1, 1), (1, 1))

    assert solution.change_light_state(mode, coordinates, light_grid_all_on) == [
        [True, True, True],
        [True, False, True],
        [True, True, True],
    ]


def test_toggle_lights(light_grid_partly_on):
    mode = "toggle"
    coordinates = ((1, 1), (2, 2))

    assert solution.change_light_state(mode, coordinates, light_grid_partly_on) == [
        [True, True, True],
        [True, False, True],
        [True, False, True],
    ]


def test_count_lit_light(light_grid_partly_on):
    mode = "toggle"
    coordinates = ((1, 1), (2, 2))

    final_light_grid = solution.change_light_state(
        mode, coordinates, light_grid_partly_on
    )
    assert sum(sum(row) for row in final_light_grid) == 7


def test_final_brightness(light_grid_varying_brightness):
    mode = "off"
    coordinates = ((0, 0), (1, 1))

    final_light_grid = solution.change_light_brightness(
        mode, coordinates, light_grid_varying_brightness
    )
    assert sum(sum(row) for row in final_light_grid) == 33
