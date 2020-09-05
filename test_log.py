import pytest

from log import log

@pytest.mark.parametrize ("a,expected", [
    (10, 2.302585092994046),
    (8000600, 15.89502709683175),
    #(-1, 'nan'),
    (None, None),
    (1.4, 0.3364722366212129),
    #(2 + 4j, 1+0.3333333333333333j),
])


def test_log(a,expected):
    assert log(a) == expected