#!/usr/bin/python3
"""Defines function that multiplies 2 matrices by
    using the module NumPy
"""

import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """Return the product of two matrices
    Args:
        m_a (list of lists of ints/floats): matrix 1
        m_b (list of lists of ints/floats): matrix 2
    """

    return (npy.matmul(m_a, m_b))
