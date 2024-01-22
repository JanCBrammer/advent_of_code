"""
--- Day 7: Internet Protocol Version 7 ---
While snooping around the local network of EBHQ,
you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited).
You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two different characters
followed by the reverse of that pair, such as `xyyx` or `abba`.
However, the IP also must not have an ABBA within any hypernet sequences,
which are contained by square brackets.

For example:

- `abba[mnop]qrst` supports TLS (`abba` outside square brackets).
- `abcd[bddb]xyyx` does not support TLS (`bddb` is within square brackets, even though `xyyx` is outside square brackets).
- `aaaa[qwer]tyui` does not support TLS (`aaaa` is invalid; the interior characters must be different).
- `ioxxoj[asdfgh]zxcvbn` supports TLS (`oxxo` is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

--- Part Two ---
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA,
anywhere in the supernet sequences (outside any square bracketed sections),
and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences.
An ABA is any three-character sequence which consists of the same character twice with a different character between them,
such as `xyx` or `aba`.
A corresponding BAB is the same characters but in reversed positions: `yxy` and `bab`, respectively.

For example:

- `aba[bab]xyz` supports SSL (`aba` outside square brackets with corresponding `bab` within square brackets).
- `xyx[xyx]xyx` does not support SSL (`xyx`, but no corresponding `yxy`).
- `aaa[kek]eke` supports SSL (`eke` in supernet with corresponding `kek` in hypernet; the `aaa` sequence is not related, because the interior character must be different).
- `zazbz[bzb]cdb` supports SSL (`zaz` has no corresponding `aza`, but `zbz` has a corresponding `bzb`, even though `zaz` and `zbz` overlap).

How many IPs in your puzzle input support SSL?

--- Notes ---

"""
from pathlib import Path
from typing import Generator
import re


def parse_input(input_path: str) -> Generator[str, None, None]:
    with Path(input_path).open() as file:
        for ip in file:
            yield ip.strip()

    return None


# TLS


def string_contains_abba(string: str) -> bool:
    if len(string) < 4:
        return False
    for i in range(len(string) - 3):
        if (
            string[i] == string[i + 3]
            and string[i + 1] == string[i + 2]
            and string[i] != string[i + 1]
        ):
            return True
    return False


def abba_outside_brackets(ip: str) -> bool:
    for section in re.split(r"\[.*?\]", ip):
        if string_contains_abba(section):
            return True
    return False


def abba_inside_brackets(ip: str) -> bool:
    for section in re.findall(r"\[([a-z]*)\]", ip):
        if string_contains_abba(section):
            return True
    return False


def ip_supports_tls(ip: str) -> bool:
    return abba_outside_brackets(ip) and (not abba_inside_brackets(ip))


def count_ips_supporting_tls(input_path: str) -> int:
    return sum(ip_supports_tls(ip) for ip in parse_input(input_path))


# SSL


def find_abas_in_ip(ip: str) -> list[str]:
    abas: list[str] = []
    if len(ip) < 3:
        return abas
    for section in re.split(r"\[.*?\]", ip):
        for i in range(len(section) - 2):
            if (section[i] == section[i + 2]) and (section[i] != section[i + 1]):
                abas.append(section[i : i + 3])
    return abas


def ip_contains_bab(ip: str, aba: str) -> bool:
    bab: str = aba[1] + aba[0] + aba[1]
    for section in re.findall(r"\[([a-z]*)\]", ip):
        if bab in section:
            return True
    return False


def ip_supports_ssl(ip: str) -> bool:
    abas = find_abas_in_ip(ip)
    if abas:
        for aba in abas:
            if ip_contains_bab(ip, aba):
                return True
    return False


def count_ips_supporting_ssl(input_path: str) -> int:
    return sum(ip_supports_ssl(ip) for ip in parse_input(input_path))


def solve_part1(input_path: str):
    print(f"Part 1:\n{count_ips_supporting_tls(input_path)} IPs support TLS.\n")


def solve_part2(input_path: str):
    print(f"Part 2:\n{count_ips_supporting_ssl(input_path)} IPs support SSL.\n")


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
