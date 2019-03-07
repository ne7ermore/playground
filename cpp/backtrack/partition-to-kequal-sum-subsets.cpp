/**
Given an array of integers nums and a positive integer k, 
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
 * **/

#include <vector>

using namespace std;

class Solution
{
  public:
    bool canPartitionKSubsets(vector<int> &nums, int k)
    {
        int sums = 0;
        for (auto &n : nums)
            sums = sums + n;
        if (k == 0 || sums % k != 0)
            return false;
        int target = sums / k;
        vector<bool> used(nums.size(), false);
        return backtrack(0, k, used, nums, target, 0);
    }

    bool backtrack(int idx, int k, vector<bool> &used, vector<int> nums, int target, int progress)
    {
        if (k == 1)
            return true;

        if (progress == target)
            return backtrack(0, k - 1, used, nums, target, 0);

        for (int i = idx; i < nums.size(); i++)
        {
            if (!used[i])
            {
                used[i] = true;
                if (backtrack(i + 1, k, used, nums, target, progress + nums[i]))
                    return true;
                used[i] = false;
            }
        }
        return false;
    }
};