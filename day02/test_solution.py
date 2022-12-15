import pytest
from . import solution


@pytest.mark.parametrize(
    "present_dimensions, wrapping_paper_area",
    [
        ([2, 3, 4], 58),
        ([1, 1, 10], 43),
    ],
)
def test_compute_wrapping_paper_area(
    present_dimensions: list[int, int, int], wrapping_paper_area: int
):

    assert (
        solution.compute_wrapping_paper_area(present_dimensions) == wrapping_paper_area
    )


@pytest.mark.parametrize(
    "present_dimensions, ribbon_length",
    [
        ([2, 3, 4], 34),
        ([1, 1, 10], 14),
    ],
)
def test_compute_ribbon_length(
    present_dimensions: list[int, int, int], ribbon_length: int
):

    assert solution.compute_ribbon_length(present_dimensions) == ribbon_length
