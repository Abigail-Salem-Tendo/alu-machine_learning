#!/usr/bin/env python3
"""Concatenate NumPy matrices along a specified axis."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a new NumPy array formed by concatenating two matrices."""
    return np.concatenate((mat1, mat2), axis=axis)
