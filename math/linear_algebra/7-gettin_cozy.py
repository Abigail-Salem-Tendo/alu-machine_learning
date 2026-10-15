#!/usr/bin/env python3
"""This module concatenaates two matrices on the same axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """This function concatenates matrices"""
    if axis == 0:
        # check if the columns match
        if len(mat1[0]) != len(mat2[0]):
            return None

        # create a new matrix
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    elif axis == 1:
        # the number of rows must match
        if len(mat1) != len(mat2):
            return None

        # create a new matrix
        result = []

        for i in range(len(mat1)):
            result.append(mat1[i][:] + mat2[i][:])
        return result
    return None
