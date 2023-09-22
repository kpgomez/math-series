import pytest
from sum_series_package.sum_series_module import sum_series

#@pytest.mark.skip()
def test_sum_series_exists():
    assert sum_series


#@pytest.mark.skip()
def test_sum_series_index_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_ten():
    actual = sum_series(10)
    expected = 55
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_zero_first_int_four_second_int_three():
    actual = sum_series(0, 4, 3)
    expected = 4
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_one_first_int_four_second_int_three():
    actual = sum_series(1, 4, 3)
    expected = 3
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_two_first_int_four_second_int_three():
    actual = sum_series(2,4,3)
    expected = 7
    assert actual == expected


#@pytest.mark.skip()
def test_sum_series_index_ten_first_int_four_second_int_three():
    actual = sum_series(10,4,3)
    expected = 301
    assert actual == expected