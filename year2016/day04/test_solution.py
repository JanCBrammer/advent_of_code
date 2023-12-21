import pytest
from . import solution


@pytest.fixture
def room_encryptions():
    return [
        ("aaaaabbbzyx", "123", "abxyz"),
        ("abcdefgh", "987", "abcde"),
        ("notarealroom", "404", "oarel"),
        ("totallyrealroom", "200", "decoy"),
    ]


def test_sum_real_room_sector_ids(room_encryptions):
    assert solution.sum_real_room_sector_ids(room_encryptions) == 1514


def test_decrypt_name():
    assert solution.decrypt_name("qzmt-zixmtkozy-ivhz", "343") == "very encrypted name"
