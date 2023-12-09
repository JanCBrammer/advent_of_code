import pytest
from . import solution


@pytest.mark.parametrize(
    "foo, bar",
    [
        ("baz", 42),
    ],
)
def test_find_bar(foo: str, bar: int):
    assert solution.find_bar(foo) == bar
