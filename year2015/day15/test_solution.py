import pytest
from math import comb
from . import solution


@pytest.fixture
def ingredient_properties():
    return [
        (-1, 2),  # capacity
        (-2, 3),  # durability
        (6, -2),  # flavor
        (3, -1),  # texture
        (8, 3),  # calories
    ]


@pytest.mark.parametrize(
    "n_ingredients, n_tablespoons, compositions",
    [
        (2, 3, [(3, 0), (2, 1), (1, 2), (0, 3)]),
        (
            3,
            3,
            [
                (3, 0, 0),
                (2, 1, 0),
                (2, 0, 1),
                (1, 2, 0),
                (1, 1, 1),
                (1, 0, 2),
                (0, 3, 0),
                (0, 2, 1),
                (0, 1, 2),
                (0, 0, 3),
            ],
        ),
    ],
)
def test_teaspoon_compositions(
    n_ingredients: int, n_tablespoons: int, compositions: list[tuple[int, ...]]
):

    assert (
        list(solution.compose_teaspoons(n_ingredients, n_tablespoons)) == compositions
    )


@pytest.mark.parametrize(
    "n_ingredients, n_tablespoons",
    [
        (2, 3),
        (4, 100),
        (5, 100),
    ],
)
def test_number_of_teaspoon_compositions(n_ingredients: int, n_tablespoons: int):

    assert len(list(solution.compose_teaspoons(n_ingredients, n_tablespoons))) == comb(
        n_ingredients + n_tablespoons - 1, n_tablespoons
    )


@pytest.mark.parametrize(
    "ingredient_properties, property_score",
    [
        ((-1, 2), 68),
        ((-2, 3), 80),
        ((6, -2), 152),
        ((3, -1), 76),
    ],
)
def test_compute_cookie_property_score(
    ingredient_properties: tuple[int, int], property_score: int
):

    assert (
        solution.compute_cookie_property_score((44, 56), ingredient_properties)
        == property_score
    )


def test_compute_cookie_score(ingredient_properties: list[tuple[int, ...]]):
    assert solution.compute_cookie_score((44, 56), ingredient_properties) == 62842880


def test_compute_cookie_score_with_calorie_constraints(
    ingredient_properties: list[tuple[int, ...]]
):
    assert (
        solution.compute_cookie_score_with_calorie_constraint(
            (40, 60), ingredient_properties
        )
        == 57600000
    )


def test_find_max_cookie_score(ingredient_properties: list[tuple[int, ...]]):

    assert (
        solution.find_max_cookie_score(
            ingredient_properties, 2, 100, solution.compute_cookie_score
        )
        == 62842880
    )


def test_find_max_cookie_score_with_calorie_constraint(
    ingredient_properties: list[tuple[int, ...]]
):

    assert (
        solution.find_max_cookie_score(
            ingredient_properties,
            2,
            100,
            solution.compute_cookie_score_with_calorie_constraint,
        )
        == 57600000
    )
