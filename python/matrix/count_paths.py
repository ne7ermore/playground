"""
Count the number of unique paths from a[0][0] to a[m-1][n-1]
We are allowed to move either right or down from a cell in the matrix.
Approaches-
(i) Recursion- Recurse starting from a[m-1][n-1], upwards and leftwards,
               add the path count of both recursions and return count.
(ii) Dynamic Programming- Start from a[0][0].Store the count in a count
                          matrix. Return count[m-1][n-1]
T(n)- O(mn), S(n)- O(mn)
"""

import numpy as np


def count_paths(m, n):
    if m < 1 or n < 1:
        return -1

    count = np.zeros((n, m))
    count[0, :] = 1
    count[:, 0] = 1

    for i in range(1, n):
        for j in range(1, m):
            count[i, j] = count[i, j-1] + count[i-1, j]

    return count[-1, -1]


if __name__ == "__main__":
    assert count_paths(3, 4) == 10
