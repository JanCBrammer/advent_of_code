import pytest
from . import solution
from typing import Final

PACKAGE_WEIGHTS: Final[list[int]] = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


@pytest.mark.parametrize(
    "n_groups, expected_quantum_entanglement",
    [(3, 99), (4, 44)],
)
def test_distribute_packages(n_groups: int, expected_quantum_entanglement: int):
    assert (
        solution.find_smallest_quantum_entanglement(PACKAGE_WEIGHTS, n_groups)
        == expected_quantum_entanglement
    )
