/**
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

[[5, 3,.,., 7,.,.,.,.],
[6,.,., 1, 9, 5,.,.,.],
[0, 9, 8,.,.,.,., 6,.],
[8,.,.,., 6,.,.,., 3],
[4,.,., 8,., 3,.,., 1],
[7,.,.,., 2,.,.,., 6],
[0, 6,.,.,.,., 2, 8,.],
[0,.,., 4, 1, 9,.,., 5],
[0,.,.,., 8,.,., 7, 9]]

A sudoku puzzle...

    [[5 3 4 6 7 8 9 1 2]
     [6 7 2 1 9 5 3 4 8]
     [1 9 8 3 4 2 5 6 7]
     [8 5 9 7 6 1 4 2 3]
     [4 2 6 8 5 3 7 9 1]
     [7 1 3 9 2 4 8 5 6]
     [9 6 1 5 3 7 2 8 4]
     [2 8 7 4 1 9 6 3 5]
     [3 4 5 2 8 6 1 7 9]]

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
 * **/

#include <vector>

using namespace std;

class Solution
{
  public:
    void solveSudoku(vector<vector<char>> &board)
    {
        backtrack(board, 0);
    }

  private:
    bool isvalid(vector<vector<char>> board, int row, int col, char c)
    {
        for (int i = 0; i < 9; i++)
        {
            if (board[row][i] != '.' && board[row][i] == c)
                return false;
            if (board[i][col] != '.' && board[i][col] == c)
                return false;
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.' &&
                board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c)
                return false;
        }
        return true;
    }

    bool backtrack(vector<vector<char>> &b, int ind)
    {
        if (ind == 81)
            return true;
        int i = ind / 9, j = ind % 9;
        if (b[i][j] != '.')
            return backtrack(b, ind + 1);
        else
        {
            for (char f = '1'; f <= '9'; f++)
            {
                if (isvalid(b, i, j, f))
                {
                    b[i][j] = f;
                    if (backtrack(b, ind + 1))
                        return true;
                    b[i][j] = '.';
                }
            }
            return false;
        }
    }
};