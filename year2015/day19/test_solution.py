import pytest
from collections import defaultdict
from . import solution


@pytest.fixture
def element_replacements_part1():
    replacements = defaultdict(set)
    replacements.update({"H": {"HO", "OH"}, "O": {"HH"}})

    return replacements


@pytest.fixture
def element_replacements_part2():
    replacements = defaultdict(str)
    replacements.update({"H": "e", "O": "e", "HO": "H", "OH": "H", "HH": "O"})

    return replacements


@pytest.mark.parametrize(
    "molecule, molecule_children",
    [
        ("HOH", {"HOOH", "HOHO", "OHOH", "HHHH"}),
        (
            "HOHOHO",
            {
                "HOHOHHH",
                "HOOHOHO",
                "HHHHOHO",
                "OHOHOHO",
                "HOHHHHO",
                "HOHOOHO",
                "HOHOHOO",
            },
        ),
    ],
)
def test_find_molecule_children(
    element_replacements_part1: dict[str, set[str]],
    molecule: str,
    molecule_children: set[str],
):
    assert (
        set(solution.find_molecule_children(element_replacements_part1, molecule))
        == molecule_children
    )


@pytest.mark.parametrize(
    "molecule, molecule_parents",
    [
        ("HOH", {"eOH", "HOe", "HeH", "HH"}),
        (
            "HOHOHO",
            {
                "eOHOHO",
                "HHOHO",
                "HeHOHO",
                "HOHeHO",
                "HOeOHO",
                "HOHOHe",
                "HOHOH",
                "HOHHO",
                "HOHOeO",
            },
        ),
    ],
)
def test_find_molecule_parents(
    element_replacements_part2: dict[str, str],
    molecule: str,
    molecule_parents: set[str],
):
    assert (
        set(solution.find_molecule_parents(element_replacements_part2, molecule))
        == molecule_parents
    )


def test_revert_molecule(element_replacements_part2: dict[str, str]):
    assert solution.revert_molecule(element_replacements_part2, "HOH") == 3
    assert solution.revert_molecule(element_replacements_part2, "HOHOHO") == 6
