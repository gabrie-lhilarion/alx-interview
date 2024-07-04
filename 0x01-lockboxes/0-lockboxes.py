def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): List of lists where each sublist represents keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # List to track which boxes have been opened
    visited[0] = True  # The first box is initially unlocked
    stack = [0]  # Stack to manage the boxes to be explored, starting with the first box

    while stack:
        current_box = stack.pop()  # Get a box to explore
        for key in boxes[current_box]:  # Iterate through the keys in the current box
            if key < n and not visited[key]:  # Check if the key opens a valid and yet unopened box
                visited[key] = True  # Mark the box as opened
                stack.append(key)  # Add the box to the stack for further exploration

    return all(visited)  # Check if all boxes have been visited (opened)
