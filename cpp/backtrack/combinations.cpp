/**
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
 * **/

#include <vector>

using namespace std;

class Solution
{
    vector<vector<int>> res;

  public:
    vector<vector<int>> combine(int n, int k)
    {
        vector<int> sub;
        backtrack(n, k, 1, sub);
        return res;
    }

    void backtrack(int n, int k, int step, vector<int> sub)
    {
        if (sub.size() == k)
        {
            res.push_back(sub);
        }
        else if (step > n || sub.size() + n - step + 1 < k)
        {
            return;
        }
        else
        {
            backtrack(n, k, step + 1, sub);
            sub.push_back(step);
            backtrack(n, k, step + 1, sub);
        }
    }
};