#!/usr/bin/env python3
"""Module contains a function to transpose a matrix"""


def matrix_transpose(matrix):
    """Return the transpose of a rectangular matrix"""
    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]
