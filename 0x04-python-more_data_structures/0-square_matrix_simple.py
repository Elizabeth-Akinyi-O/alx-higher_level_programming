#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [row[:] for row in matrix]
    for index, row in enumerate(matrix2):
        for index2, col in enumerate(matrix2):
            matrix2[index][index2] = row[index2] ** 2
    return matrix2
