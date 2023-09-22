import pytest
from fibonacci_package.fibonacci_module import fibonacci

#@pytest.mark.skip()
def test_fibonacci_exists():
    assert fibonacci


#@pytest.mark.skip()
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


#@pytest.mark.skip()
def test_fibonacci_twenty():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected


