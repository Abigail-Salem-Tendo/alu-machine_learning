#!/usr/bin/env python3
"""Module for calculating the sum of squared integers."""


def summation_i_squared(n):
    """Calculate the sum of squares from 1 to n without loops."""
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        return None

    if not isinstance(n, int) or n < 1:
        return None

    return n * (n + 1) * (2 * n + 1) // 6
