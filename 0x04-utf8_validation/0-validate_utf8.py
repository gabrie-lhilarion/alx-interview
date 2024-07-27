#!/usr/bin/python3
"""
A script to validate if a given data set represents valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if the data is valid UTF-8, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7

        if num_bytes == 0:
            """
            Determine the number of bytes in the UTF-8 character.
            The number of leading 1s in the first byte determines the number
            of bytes in the UTF-8 character.
            """
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                # Single-byte character (0xxxxxxx) which is valid
                continue

            # Invalid scenarios for UTF-8:
            # 1. num_bytes == 1 indicates a char of 2 bytes (invalid case).
            # 2. num_bytes > 4 it exceeds maximum length of a UTF-8 character.
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            """
            For multi-byte characters, ensure each subsequent byte has
            the format 10xxxxxx.
            """
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to be processed
        num_bytes -= 1

    # If there are leftover bytes, it's an invalid UTF-8 encoding
    return num_bytes == 0
