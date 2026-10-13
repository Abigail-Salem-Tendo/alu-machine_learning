#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a square matrix."""


def cofactor(matrix):
    """Calculate the cofactor matrix of a square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor = __import__('1-minor').minor
    size = len(matrix)
    minor_matrix = minor(matrix)
    cofactor_matrix = []

    for row in range(size):
        cofactor_row = []

        for column in range(size):
            sign = (-1) ** (row + column)
            cofactor_row.append(sign * minor_matrix[row][column])

        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix
