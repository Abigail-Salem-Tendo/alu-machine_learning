#!/usr/bin/env python3
"""Module for calculating the inverse of a square matrix."""


def inverse(matrix):
    """Calculate the inverse of a square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    determinant = __import__('0-determinant').determinant
    det = determinant(matrix)

    if det == 0:
        return None

    if len(matrix) == 1:
        return [[1 / matrix[0][0]]]

    adjugate = __import__('3-adjugate').adjugate
    adj = adjugate(matrix)

    inverse_matrix = []

    for row in range(len(matrix)):
        new_row = []

        for column in range(len(matrix)):
            new_row.append(adj[row][column] / det)

        inverse_matrix.append(new_row)

    return inverse_matrix
