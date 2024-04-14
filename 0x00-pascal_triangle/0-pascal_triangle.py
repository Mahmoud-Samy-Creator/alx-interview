#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list of lists: Pascal's triangle represented
    as a list of lists, where each sublist
    corresponds to a row in Pascal's triangle.
    Each sublist contains the integers of that row.
    """
    if n <= 0:
        return []
    else:
        traingle = []
        for i in range(n):
            row = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                elif i >= 2:
                    row.append(traingle[i - 1][j] + traingle[i - 1][j - 1])
                else:
                    row.append(i)
            traingle.append(row)
    return traingle
