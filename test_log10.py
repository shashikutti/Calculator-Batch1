import pytest

from calc import log10


@pytest.mark.parametrize("a, expected", [
    (100.12, 2.0005208409361854),
    (1.4, 0.146128035678238),
    (10000000000000000000000000000000000000000.4, 40.0),
    (88**88, 171.11447514921483),
]
)
def test_log10(a,  expected):
    assert log10(a) == expected


@pytest.mark.parametrize("a", [
    (None, None),
    ('1', '1'),
    (-120, -120),
    (2 + 3j, 2 + 3j)
])
def test_negative(a):
    with pytest.raises(TypeError):
        log10(a)