#!/usr/bin/env python3
"""Perform element-wise arithmetic operations on NumPy arrays."""

import numpy as np


def np_elementwise(mat1, mat2):
    """Return the element-wise sum, difference, product, and quotient."""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
