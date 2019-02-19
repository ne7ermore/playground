/**
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
**/

#include <vector>

class Solution
{
  public:
    bool searchMatrix(std::vector<std::vector<int>> &matrix, int target)
    {
        if (matrix.size() < 1 || matrix[0].size() < 1)
            return false;

        int row = matrix[0].size() - 1;
        int col = 0;

        while (row >= 0 && col < matrix.size())
        {
            if (matrix[col][row] == target)
                return true;

            else if (matrix[col][row] > target)
                row--;

            else if (matrix[col][row] < target)
                col++;
        }

        return false;
    }
};