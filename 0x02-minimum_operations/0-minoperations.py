#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """
    calculates the fewest number of operations needed
    """
    num, sum = n, 0
    while (num != 1):
        if num % 2 == 0:
            sum += 2
            num /= 2
        else:
            sum += 3
            num /= 3
    return sum
