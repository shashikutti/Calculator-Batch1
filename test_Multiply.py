import pytest

from multiply import multiply


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (8000600, 6405006, 51243891003600),
    (-1, -2, 2),
    (-50, 2, -100),
    (-2**5, -9**9, 12397455648),
    (2, 0, 0),
    (100**9, 150**5, 75937500000000000000000000000),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
