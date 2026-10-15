#!/usr/bin/env python3
"""Module for calculating the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if any(not isinstance(coef, (int, float)) or isinstance(coef, bool)
           for coef in poly):
        return None

    derivative = []

    for power in range(1, len(poly)):
        derivative.append(power * poly[power])

    if not derivative or all(coef == 0 for coef in derivative):
        return [0]

    return derivative
