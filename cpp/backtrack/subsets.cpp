/**
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
 * **/

#include <vector>

using namespace std;

class Solution
{
    vector<vector<int>> res;

  public:
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        vector<int> sub;
        backtrack(nums, sub, 0);
        return res;
    }

    void backtrack(vector<int> &nums, vector<int> sub, int step)
    {
        if (step == nums.size())
        {
            if (find(res.begin(), res.end(), sub) == res.end())
                res.push_back(sub);
        }
        else
        {
            backtrack(nums, sub, step + 1);
            sub.push_back(nums[step]);
            backtrack(nums, sub, step + 1);
        }
    }
};