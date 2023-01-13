#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    squared_matrix = []
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(0)
        squared_matrix.append(row)

    for i in range(rows):
        for j in range(cols):
            squared_matrix[i][j] = matrix[i][j] ** 2
    return squared_matrix
