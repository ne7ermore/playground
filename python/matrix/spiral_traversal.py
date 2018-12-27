"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

import numpy as np


def skip(matrix, direction, i, j, res):
    n, m = matrix.shape
    if direction == 0:
        while j < m:
            res.append(matrix[i, j])
            j += 1
        matrix = matrix[i+1:, :]
        n, m = matrix.shape
        return matrix, 0, m-1, 1

    elif direction == 1:
        while i < n:
            res.append(matrix[i, j])
            i += 1
        matrix = matrix[:, :m-1]
        n, m = matrix.shape
        return matrix, n-1, m-1, 2

    elif direction == 2:
        while j >= 0:
            res.append(matrix[i, j])
            j -= 1

        matrix = matrix[:n-1, :]
        n, m = matrix.shape
        return matrix, n-1, 0, 3
    else:
        while i >= 0:
            res.append(matrix[i, j])
            i -= 1
        return matrix[:, j+1:], 0, 0, 0


def spiral_traversal(matrix):
    res, direction = [], 0
    n, m = matrix.shape
    i, j = 0, 0
    while len(res) < n*m:
        matrix, i, j, direction = skip(matrix, direction, i, j, res)

    return res


if __name__ == "__main__":
    mat = np.asarray([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    assert spiral_traversal(
        mat) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
