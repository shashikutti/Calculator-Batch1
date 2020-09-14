import pytest

from calc_model import add


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (8000600, 6405006, 14405606),
    (-1, 2, 1),
    (1.4, 1.6, 3.0),
    (2 ** 100, 88 ** 88, 1.3015928349429721e+171),
    (1, '2', 3),
    ('1', '2', 3),
    ('1', 2, 3),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b", [
    (None, None),
    (None, 20),
    (30, None),
    ('first', 'second'),
    # (2 + 3j, 3 + 5j)
])
def test_negative(a, b):
    with pytest.raises(ValueError):
        add(a, b)
