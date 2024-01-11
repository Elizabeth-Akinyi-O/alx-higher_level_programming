#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # copy every item from the input matrix
    newmatrix = [row[:] for row in matrix]
    for idx, row in enumerate(newmatrix):
        for idx2, col in enumerate(newmatrix):
            newmatrix[idx][idx2] = row[idx2] ** 2
    return newmatrix
