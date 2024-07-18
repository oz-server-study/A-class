# test_param.py
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (1, 2, 3),
    # (1, 2, 4),
])
def test_addition(a, b, expected):
    assert a + b == expected
