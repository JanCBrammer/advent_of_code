from . import solution


def test_find_password_part1():
    assert solution.find_password_part1("abc") == "18f47a30"


def test_find_password_part2():
    assert solution.find_password_part2("abc") == "05ace8e3"
