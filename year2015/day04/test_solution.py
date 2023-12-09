import pytest
from . import solution


@pytest.mark.parametrize(
    "secret_key, salt",
    [
        ("abcdef", 609043),
        ("pqrstuv", 1048970),
    ],
)
def test_solve_part1(secret_key: str, salt: int):
    assert solution.solve(secret_key, "00000") == salt
