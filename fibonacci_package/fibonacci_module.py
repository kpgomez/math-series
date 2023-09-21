"""
Fibonacci sequence starts with 0,1 and each new iteration is a sum of the two integers before it
0+1=2, 1+2=3, 2+3=5 so the first five integers are 0, 1, 2, 3, 5
"""


def fibonacci(n):
    """
    Returns the integer at index n
    :param n: integer
    :return: integer
    """
    # base case 1

    if n == 0:
        return 0

    # base case 2 (when I had base case if n <= 1 return 1, the value was off by one index)
    if n == 1:
        return 1

    # recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)