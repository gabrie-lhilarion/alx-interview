#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number
of operations needed to result in exactly `n` 'H' characters
in a text file. The operations allowed are 'Copy All' and 'Paste'.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to
    result in exactly n 'H' characters in the file.

    :param n: int - The desired number of 'H' characters.
    :return: int - The minimum number of operations required
    or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # Check for smallest divisor and divide n by
        # that divisor until it's no longer divisible
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
