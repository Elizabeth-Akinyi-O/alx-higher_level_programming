#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [row[:] for row in matrix]
    for idx, row in enumerate(matrix2):
        for idx2, col in enumerate(matrix2):
            matrix2[idx][idx2] = row[idx2] ** 2
    return matrix2
