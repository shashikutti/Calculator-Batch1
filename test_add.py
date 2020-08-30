import pytest

from add import add


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (8000600, 6405006, 14405606),
    (-1, 2, 1),
    (None, None, None),
    (None, 20, 20),
    (30, None, 30),
    (1.4, 1.6, 3.0),
    (2 + 3j, 3 + 5j, 5 + 8j),
    (2 ** 100, 88 ** 88, 1301592834942972055182648307417315364538725075960067827915311484722452340966317215805106820959190833309704934346517741237438752456673499160126892065596119340605651782991872)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# def test_add_characters():
#     return_value = add(1, '2')
#     print(type(return_value))
#     assert return_value == '12'
