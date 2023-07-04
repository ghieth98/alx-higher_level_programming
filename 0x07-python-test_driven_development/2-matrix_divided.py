#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    for x in matrix:
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of matrix must have same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be matrix (list of lists) of integers/floats")

    if not (isinstance(div, (int, float))):
        raise TypeError("div must be number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div, 2) for y in x] for x in matrix]
