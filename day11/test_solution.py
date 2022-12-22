import pytest
from . import solution


@pytest.mark.parametrize(
    "password, incremented_password",
    [
        ("y", "z"),
        ("z", "a"),
        ("zz", "aa"),
        ("zy", "zz"),
        ("xyz", "xza"),
    ],
)
def test_increment_password(password: str, incremented_password: str):

    assert solution.increment_password(password) == incremented_password


@pytest.mark.parametrize(
    "password, valid",
    [
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdefgh", False),
        ("abcdffaa", True),
        ("ghijklmn", False),
        ("ghjaabcc", True),
        ("ghjaaabc", False),
        ("jjmm", False),
    ],
)
def test_password_is_valid(password: str, valid: bool):

    assert solution.password_is_valid(password) == valid
