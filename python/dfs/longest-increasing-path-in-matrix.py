"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


def longestIncreasingPath(self, M):
    if not any(M):
        return 0
    d = {}

    def check(i, j):
        if not (i, j) in d:
            d[(i, j)] = max(check(x, y) if 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y]
                            > M[i][j] else 0 for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]) + 1
        return d[(i, j)]
    return max(check(i, j) for i in range(len(M)) for j in range(len(M[0])))
