#!/usr/bin/env python3
"""Module for integrating polynomials."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int) or isinstance(C, bool):
        return None

    if any(not isinstance(coef, (int, float)) or isinstance(coef, bool)
           for coef in poly):
        return None

    integral = [C]

    for power, coef in enumerate(poly):
        result = coef / (power + 1)
        if result.is_integer() if isinstance(result, float) else False:
            result = int(result)
        integral.append(result)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
