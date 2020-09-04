import pytest

from MultiplayFunctions import multiplying

billy = 5
bob = 10
joe = 15
ven = 20
kat = 25


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (8000600, 6405006, 51243891003600),
    (billy, bob, 50),
    (billy, 5, 25),
    (ven, kat, 500),


])
def test_multiply(a, b, expected):
    assert multiplying(a, b) == expected


