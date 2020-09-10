import pytest


def divide(a, b):
    type1 = type(a)
    type2 = type(b)

    if a is None:
        return b

    if b is None:
        return a

    if type1 is not int:
        raise TypeError('First input parameter must be an int. Instead it is ' + str(type1))

    if type2 is not int:
        raise TypeError('Second input parameter must be an int. Instead it is ' + str(type2))

    return a / b


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
    assert divide(a, b) == expected
