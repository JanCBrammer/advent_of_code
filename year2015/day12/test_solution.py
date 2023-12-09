import json
import pytest
from . import solution


@pytest.mark.parametrize(
    "document, document_sum",
    [
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ],
)
def test_add_numbers(document: str, document_sum: int):
    assert solution.add_numbers(document) == document_sum


@pytest.mark.parametrize(
    "document, document_sum",
    [
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ],
)
def test_add_numbers_conditionally(document: str, document_sum: int):
    json_document = json.loads(document)

    assert sum(solution.add_numbers_conditionally(json_document)) == document_sum
