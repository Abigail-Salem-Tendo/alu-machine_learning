#!/usr/bin/env python3
"""Module for calculating the determinant of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    size = len(matrix)

    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0

    for column in range(size):
        minor = []

        for row in matrix[1:]:
            minor_row = row[:column] + row[column + 1:]
            minor.append(minor_row)

        sign = (-1) ** column
        det += sign * matrix[0][column] * determinant(minor)

    return det
