#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): a list of lists of integers or floats
        div (integer or float): must be a number
    Returns:
         a new matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    # m_row - matrix row && m_col - matrix column
    for m_row in matrix:
        if len(m_row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for m_col in m_row:
            if type(m_col) is not int and type(m_col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for m_row in matrix:
        len_rows.append(len(m_row))
    if not all(m_col == len_rows[0] for m_col in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(m_col/div, 2) for m_col in m_row] for m_row in matrix]

    return (new_matrix)
