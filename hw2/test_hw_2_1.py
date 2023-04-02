import pytest

from hw_2_1 import major_and_minor_elem

LISTS = [
    ([2, 2, 1, 1, 1, 2, 2], (2, 1)), 
    ([3, 2, 3], (3, 2)),
    ([3, 3, 2, 2, 3, 3, 1], (3, 1))
]

print(LISTS)

@pytest.mark.parametrize(
    "numbers, expected", LISTS
)
def test_major_and_minor_elem(numbers, expected):
    assert major_and_minor_elem(numbers) == expected

