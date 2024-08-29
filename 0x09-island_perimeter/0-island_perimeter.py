#!/usr/bin/env python3
"""
This module provides a function to calculate the perimeter of an island
represented in a grid.

The grid is a list of lists of integers where:
- 0 represents water
- 1 represents land

Each cell is square with a side length of 1, and cells are connected
horizontally or vertically (not diagonally). The grid is completely
surrounded by water, contains only one island, and has no lakes (water
inside that isn't connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List of list of integers where 0 represents
    water and 1 represents land.
    :return: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
