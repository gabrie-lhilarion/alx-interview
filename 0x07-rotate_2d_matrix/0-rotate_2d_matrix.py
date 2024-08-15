#!/usr/bin/env python3

"""
This module provides a function to rotate a 2D n x n
matrix 90 degrees clockwise in-place. The function
modifies the matrix directly without returning any value.

The rotation is done in two steps:
1. Transpose the matrix (convert rows to columns).
2. Reverse each row of the transposed matrix.

Function:
    - rotate_2d_matrix(matrix) -> None:
    Rotates the matrix in-place.
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate the given n x n matrix 90 degrees
    clockwise in-place.

    Args:
        matrix: The matrix to rotate, represented
        as a list of lists.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
