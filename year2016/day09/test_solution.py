import pytest
from . import solution


@pytest.mark.parametrize(
    "compressed, markers",
    [
        ("ADVENT", []),
        ("A(1x5)BC", [solution.Marker(1, 6, 1, 5)]),
        ("(3x3)XYZ", [solution.Marker(0, 5, 3, 3)]),
        (
            "A(2x2)BCD(2x2)EFG",
            [solution.Marker(1, 6, 2, 2), solution.Marker(9, 14, 2, 2)],
        ),
        ("(6x1)(1x3)A", [solution.Marker(0, 5, 6, 1)]),
        (
            "X(8x2)(3x3)ABCY",
            [solution.Marker(1, 6, 8, 2)],
        ),
    ],
)
def test_get_markers(compressed: str, markers):
    assert solution.get_markers(compressed) == markers


def test_get_length_decompressed_marker():
    marker = solution.Marker(0, 5, 3, 3)
    assert solution.get_length_decompressed_marker(marker) == 1


@pytest.mark.parametrize(
    "compressed, n_decompressed_chars",
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ],
)
def test_get_length_decompressed_sequence(compressed: str, n_decompressed_chars: int):
    assert (
        solution.get_length_decompressed_sequence_part1(compressed)
        == n_decompressed_chars
    )


@pytest.mark.parametrize(
    "compressed, n_decompressed_chars",
    [
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
)
def test_get_length_decompressed_sequence_part2(
    compressed: str, n_decompressed_chars: int
):
    assert (
        solution.get_length_decompressed_sequence_part2(compressed)
        == n_decompressed_chars
    )
