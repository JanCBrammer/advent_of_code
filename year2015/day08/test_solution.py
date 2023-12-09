import pytest
from collections import namedtuple
from . import solution


@pytest.mark.parametrize(
    "line, char_count",
    [
        (r'""', solution.CharCounts(2, 0, 6)),
        (r'"abc"', solution.CharCounts(5, 3, 9)),
        (r'"aaa\"aaa"', solution.CharCounts(10, 7, 16)),
        (r'"\x27"', solution.CharCounts(6, 1, 11)),
    ],
)
def test_count_chars(line: str, char_count: namedtuple):
    assert solution.count_chars(line) == char_count
