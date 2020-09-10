import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 2),
    (3600, 400, 9),
    (-10, 5, -2),
    (None, None, None),
    (None, 20, 20),
    (30, None, 30),
    (44338994, 9562, 4637),
    (9**4, 3**5, 27),
    (8**2, 2**3, 8)
])
def test_divide(a, b, expected):
    assert test_divide(a, b) == expected
