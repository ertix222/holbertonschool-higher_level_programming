#!/usr/bin/python3

"""
This module defines a function, `matrix_divided(matrix, div)`
which divides all elements of a matrix by a given divisor.
The result is returned as a new matrix
with all values rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(elem, (int, float)) for row in matrix for elem in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
