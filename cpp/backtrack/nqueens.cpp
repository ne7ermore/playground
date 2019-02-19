/**
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
**/

#include <vector>

class Solution
{
  public:
    int totalNQueens(int n)
    {
        int count = 0;
        std::vector<int> place;
        backtrack(n, 0, count, place);
        return count;
    }

  private:
    bool isvalid(std::vector<int> place)
    {
        int rowid = place.size() - 1;
        for (int i = 0; i < rowid; i++)
        {
            int diff = abs(place[i] - place[rowid]);
            if (diff == 0 || diff == rowid - i)
                return false;
        }
        return true;
    }

    void backtrack(int row, int n, int &count, std::vector<int> &place)
    {
        if (row == n)
            count++;
        else
        {
            n++;
            for (int i = 0; i < row; i++)
            {
                place.push_back(i);
                if (isvalid(place))
                {
                    backtrack(row, n, count, place);
                }
                place.pop_back();
            }
        }
    }
};