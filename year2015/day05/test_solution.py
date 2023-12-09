import pytest
from . import solution


@pytest.mark.parametrize(
    "string, nice",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_string_is_nice_part1(string: str, nice: bool):
    assert solution.string_is_nice(string, solution.RULES_PART1) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_string_is_nice_part2(string: str, nice: bool):
    assert solution.string_is_nice(string, solution.RULES_PART2) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", True),
        ("dvszwmarrgswjxmb", True),
    ],
)
def test_string_contains_repeated_letter(string: str, nice: bool):
    assert solution.string_contains_repeated_letter(string) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", True),
        ("haegwjzuvuyypxyu", True),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_string_contains_vowels(string: str, nice: bool):
    assert solution.string_contains_vowels(string) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", True),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", True),
    ],
)
def test_string_free_of_forbidden_substring(string: str, nice: bool):
    assert solution.string_free_of_forbidden_substrings(string) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", True),
        ("ieodomkazucvgmuy", False),
        ("aaa", False),
    ],
)
def test_string_contains_repeated_letter_pair(string: str, nice: bool):
    assert solution.string_contains_repeated_letter_pair(string) == nice


@pytest.mark.parametrize(
    "string, nice",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", True),
        ("aaa", True),
        ("aab", False),
    ],
)
def test_string_contains_separated(string: str, nice: bool):
    assert solution.string_contains_separated_repeated_letter(string) == nice
