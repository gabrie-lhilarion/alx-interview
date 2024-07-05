#!/usr/bin/python3
"""
Module: canUnlockAll

This module provides a function to determine if all
boxes in a given list can be opened.
Each box contains keys to other boxes.
The function uses a breadth-first search (BFS)
or depth-first search (DFS) approach to
explore the boxes and keys.

Function:
    canUnlockAll(boxes): Determines if all boxes c
    an be opened given the initial set of keys.

Example:
    >>> canUnlockAll([[1], [2], [3], []])
    True
    >>> canUnlockAll([[1, 3], [3, 0, 1], [2], [0]])
    False
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): List of lists where each sublist
        represents keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
