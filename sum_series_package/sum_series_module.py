"""
Sum series takes in one required parameter and two optional parameters. The required parameter will
determine which element in the series to print. The two optional parameters will have default values of 0
and 1, and will determine the first two values for the series to be produced.
"""


def sum_series(n, x1=0, x2=1):
    """
    Returns the integer at index n
    :param n: integer
    :param x1: integer
    :param x2: integer
    :return: integer
    """

    # base case 1
    if n == 0:
        return x1

    # base case 2
    if n == 1:
        return x2
    # base case 3, before I added this it was returning x2
    if n == 2:
        return x1 + x2

    # def test_sum_series_index_ten_first_int_four_second_int_three() failed when x1, x2 params were missing because it was using default values
    ## recursive case
    else:
        return sum_series(n-1, x1, x2) + sum_series(n-2, x1, x2)
