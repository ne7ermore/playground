"""
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
Example:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

import numpy as np


def multiply(a, b):
    ar, ae = a.shape
    br, be = b.shape
    assert ae == br

    c = np.zeros([ar, be])

    for i, arow in enumerate(a):
        for j, aelem in enumerate(arow):
            if aelem:
                for k, belem in enumerate(b[j]):
                    if belem:
                        c[i, k] += belem*aelem

    return c


if __name__ == "__main__":
    a = np.array([[1, 0, 0],
                  [-1, 0, 3]])

    b = np.array([[7, 0, 0],
                  [0, 0, 0],
                  [0, 0, 1]])

    print(multiply(a, b))
