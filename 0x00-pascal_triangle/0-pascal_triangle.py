#!/usr/bin/python3

"""
This script defines a function to generate Pascal's triangle up to n rows.

Usage:
    You can run this script directly to see Pascal's triangle printed for a specific value of n.

Example:
    $ python3 pascal_triangle.py
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists of integers
        representing Pascal's triangle.
        Each sublist represents a row in the triangle.


    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
