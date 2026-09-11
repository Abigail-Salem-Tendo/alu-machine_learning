#!/usr/bin/env python3
def matrix_shape(matrix):
    """Return the dimensions of a nested list as a list of integers"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
