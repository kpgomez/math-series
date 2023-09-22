"""
Lucas series starts with 2, 1 and each new iteration is a sum of the two integers before it
2+1=3, 3+1=4, 4+3=7 so the first five integers are 2, 1, 3, 4, 7
"""


def lucas(n):
    """
    Returns the integer at index n
    :param n: integer
    :return: integer
    """

    # base case 1

    if n == 0:
        return 2

    # base case 2

    if n == 1:
        return 1

    ## recursive case
    else:
        return lucas(n - 1) + lucas(n - 2)