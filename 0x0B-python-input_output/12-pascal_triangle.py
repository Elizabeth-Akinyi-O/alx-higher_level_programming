#!/usr/bin/python3
"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
        the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    # pattern of the pascal triangle
    triangle = [[1]]
    while len(triangle) != n:
        pattern = triangle[-1]
        temp = [1]
        for a in range(len(pattern) - 1):
            temp.append(pattern[a] + pattern[a + 1])
        temp.append(1)
        triangle.append(temp)
    return (triangle)
