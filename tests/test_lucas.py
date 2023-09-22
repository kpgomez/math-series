import pytest
from lucas_package.lucas_module import lucas

#@pytest.mark.skip()
def test_lucas_exists():
    assert lucas


#@pytest.mark.skip()
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_lucas_twenty():
    actual = lucas(20)
    expected = 15127
    assert actual == expected



