"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms.
Of course, the list is encrypted and full of decoy data,
but the instructions to decode the list are barely hidden nearby.
Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters
in the encrypted name, in order, with ties broken by alphabetization.
For example:

- `aaaaa-bbb-z-y-x-123[abxyz]` is a real room because
    the most common letters are `a` (5), `b` (3),
    and then a tie between `x`, `y`, and `z`, which are listed alphabetically.
- `a-b-c-d-e-f-g-h-987[abcde]` is a real room because although the letters are all tied
    (1 of each), the first five are listed alphabetically.
- `not-a-real-room-404[oarel]` is a real room.
- `totally-real-room-200[decoy]` is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher,
which is nearly unbreakable without the right software.
However, the information kiosk designers at Easter Bunny HQ
were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet
a number of times equal to the room's sector ID.
`A` becomes `B`, `B` becomes `C`, `Z` becomes `A`, and so on.
Dashes become spaces.

For example, the real name for `qzmt-zixmtkozy-ivhz-343` is `very encrypted name`.

What is the sector ID of the room where North Pole objects are stored?

--- Notes ---

"""
from pathlib import Path
from typing import Generator, Iterable
from collections import Counter


def parse_input(input_path: str) -> Generator[tuple[str, str, str], None, None]:
    with Path(input_path).open() as input_file:
        for line in input_file:
            line = line.strip()
            name = line[:-11]
            sector_id = line[-10:-7]
            checksum = line[-6:-1]

            yield (name, sector_id, checksum)

    return None


def filter_real_rooms(
    room_encryptions: Iterable[tuple[str, str, str]]
) -> Generator[tuple[str, str, str], None, None]:
    for name, sector_id, checksum in room_encryptions:
        letter_counts = sorted(
            list(Counter(name.replace("-", "")).items()), key=lambda i: (-i[1], i[0])
        )[:5]

        if checksum == "".join(i[0] for i in letter_counts):
            yield (name, sector_id, checksum)

    return None


def decrypt_name(name: str, sector_id: str) -> str:
    return "".join(
        chr((ord(c) - ord("a") + int(sector_id)) % 26 + ord("a")) if c != "-" else " "
        for c in name
    )


def decrypt_room_names(
    room_encryptions: Generator[tuple[str, str, str], None, None]
) -> Generator[tuple[str, str, str], None, None]:
    for name, sector_id, checksum in room_encryptions:
        yield (decrypt_name(name, sector_id), sector_id, checksum)

    return None


def sum_real_room_sector_ids(room_encryptions: Iterable[tuple[str, str, str]]) -> int:
    return sum(
        int(sector_id) for _, sector_id, _ in filter_real_rooms(room_encryptions)
    )


def solve_part1(input_path: str):
    sector_id_sum = sum_real_room_sector_ids(parse_input(input_path))
    print(f"Part 1:\nThe sum of the sector IDs of the real rooms is {sector_id_sum}.\n")


def solve_part2(input_path: str):
    for name, sector_id, _ in decrypt_room_names(
        filter_real_rooms(parse_input(input_path))
    ):
        if "north" in name:
            print(
                f"Part 2:\nThe sector ID of the room where North Pole objects are stored is {sector_id}.\n"
            )
            break


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
