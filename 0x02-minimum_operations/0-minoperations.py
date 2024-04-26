#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """
    calculates the fewest number of operations needed
    """
    if not isinstance(n, int):
        return 0
    num, sum, x = n, 0, 2
    while (num > 1):
        if num % x == 0:
            num /= x
            sum += 2
        else:
            x += 1
    return sum
