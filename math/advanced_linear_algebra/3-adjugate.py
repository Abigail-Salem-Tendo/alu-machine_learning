#!/usr/bin/env python3
"""Module for calculating the adjugate matrix."""


def adjugate(matrix):
    """Calculate the adjugate matrix of a square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor = __import__('2-cofactor').cofactor
    cofactor_matrix = cofactor(matrix)

    adjugate_matrix = []

    for column in range(len(matrix)):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(cofactor_matrix[row][column])

        adjugate_matrix.append(new_row)

    return adjugate_matrix
