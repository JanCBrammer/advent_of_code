import pytest
from . import solution


@pytest.mark.parametrize(
    "ip, expected_outcome",
    [
        ("abba[abba]qrst", True),
        ("yabba[abba]qrst", True),
        ("abbay[abba]qrst", True),
        ("yabbay[abba]qrst", True),
        ("aaaa[abba]tyui", False),
    ],
)
def test_abba_outside_brackets(ip: str, expected_outcome: bool):
    assert solution.abba_outside_brackets(ip) == expected_outcome


@pytest.mark.parametrize(
    "ip, expected_outcome",
    [
        ("abcd[abba]abba", True),
        ("abcd[yabba]abba", True),
        ("abcd[abbay]abba", True),
        ("abcd[yabbay]abba", True),
        ("aaaa[aaaa]tyui", False),
    ],
)
def test_abba_inside_brackets(ip: str, expected_outcome: bool):
    assert solution.abba_inside_brackets(ip) == expected_outcome


@pytest.mark.parametrize(
    "ip, expected_outcome",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_ip_supports_ssl(ip: str, expected_outcome: bool):
    assert solution.ip_supports_ssl(ip) == expected_outcome
