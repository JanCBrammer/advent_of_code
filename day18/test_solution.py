import pytest
from . import solution


@pytest.mark.parametrize(
    "n_cols, light_neighbors",
    [
        (
            3,
            (
                (1, 3, 4),
                (0, 2, 3, 4, 5),
                (1, 4, 5),
                (0, 1, 4, 6, 7),
                (0, 1, 2, 3, 5, 6, 7, 8),
                (1, 2, 4, 7, 8),
                (3, 4, 7),
                (3, 4, 5, 6, 8),
                (4, 5, 7),
            ),
        ),
        (
            4,
            (
                (1, 4, 5),
                (0, 2, 4, 5, 6),
                (1, 3, 5, 6, 7),
                (2, 6, 7),
                (0, 1, 5, 8, 9),
                (0, 1, 2, 4, 6, 8, 9, 10),
                (1, 2, 3, 5, 7, 9, 10, 11),
                (2, 3, 6, 10, 11),
                (4, 5, 9, 12, 13),
                (4, 5, 6, 8, 10, 12, 13, 14),
                (5, 6, 7, 9, 11, 13, 14, 15),
                (6, 7, 10, 14, 15),
                (8, 9, 13),
                (8, 9, 10, 12, 14),
                (9, 10, 11, 13, 15),
                (10, 11, 14),
            ),
        ),
    ],
)
def test_map_light_neighbors(n_cols: int, light_neighbors: dict[int, tuple[int, ...]]):

    assert solution.map_light_neighbors(n_cols, n_cols) == light_neighbors


@pytest.fixture
def lights() -> tuple[bool, ...]:

    return tuple(light == "#" for light in ".#.#.#...##.#....#..#...#.#..#####..")


def test_update_lights(lights: tuple[bool, ...]):

    LIGHT_NEIGHBORS = solution.map_light_neighbors(6, 6)

    for _ in range(4):
        lights = tuple(
            solution.compute_light_state(light, lights, light_neighbors)
            for light, light_neighbors in enumerate(LIGHT_NEIGHBORS)
        )

    assert sum(lights) == 4


def test_update_lights_corners_on(lights: tuple[bool, ...]):

    LIGHT_NEIGHBORS = solution.map_light_neighbors(6, 6)
    lights = solution.switch_on_grid_corners(lights, 6, 6)

    for _ in range(5):
        lights = tuple(
            solution.compute_light_state(light, lights, light_neighbors)
            for light, light_neighbors in enumerate(LIGHT_NEIGHBORS)
        )
        lights = solution.switch_on_grid_corners(lights, 6, 6)

    assert sum(lights) == 17
