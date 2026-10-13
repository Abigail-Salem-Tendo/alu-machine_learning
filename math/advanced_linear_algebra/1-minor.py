#!/usr/bin/env python3
"""Module for calculating the minor matrix of a square matrix."""


def minor(matrix):
    """Calculate the minor matrix of a square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    determinant = __import__('0-determinant').determinant
    size = len(matrix)
    minor_matrix = []

    for row_index in range(size):
        minor_row = []

        for column_index in range(size):
            submatrix = []

            for current_row in range(size):
                if current_row == row_index:
                    continue

                new_row = []

                for current_column in range(size):
                    if current_column == column_index:
                        continue

                    new_row.append(matrix[current_row][current_column])

                submatrix.append(new_row)

            minor_row.append(determinant(submatrix))

        minor_matrix.append(minor_row)

    return minor_matrix
