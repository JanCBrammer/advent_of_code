import pytest
from . import solution


@pytest.fixture
def messages():
    return (
        message
        for message in [
            "eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar",
        ]
    )


def test_recover_message_part1(messages):
    assert solution.recover_message(messages, 6, max) == "easter"


def test_recover_message_part2(messages):
    assert solution.recover_message(messages, 6, min) == "advent"
