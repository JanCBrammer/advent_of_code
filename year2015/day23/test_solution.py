import pytest
from . import solution


@pytest.fixture
def program():
    return ["inc a", "jio a, +2", "tpl a", "inc a"]


def test_run_program(program: list[str]):
    assert solution.run_program(program, {"a": 0, "b": 0}) == {"a": 2, "b": 0}
