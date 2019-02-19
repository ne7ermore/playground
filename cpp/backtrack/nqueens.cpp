// The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

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