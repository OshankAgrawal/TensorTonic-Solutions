import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    row = len(A)
    col = len(A[0])

    transpose = []
    for j in range(col):
        temp_row = []
        for i in range(row):
            temp_row.append(A[i][j])
        transpose.append(temp_row)

    return np.array(transpose)