import pytest
from . import solution


@pytest.mark.parametrize(
    "instructions, expected_n_blocks",
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ],
)
def test_find_manhattan_distance_to_hq(instructions: str, expected_n_blocks: int):
    hq_location: tuple[int, int] = solution.trace_path_to_hq(instructions)[-1]

    assert (
        solution.compute_manhattan_distance_from_origin(hq_location)
        == expected_n_blocks
    )


def test_find_manhattan_distance_to_first_recurring_location():
    path_to_hq: list[tuple[int, int]] = solution.trace_path_to_hq("R8, R4, R4, R8")
    first_recurring_location: tuple[int, int] = solution.find_first_recurring_location(
        path_to_hq
    )

    assert (
        solution.compute_manhattan_distance_from_origin(first_recurring_location) == 4
    )
