#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists of integers
        representing Pascal's triangle.
        Each sublist represents a row in the triangle.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
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
