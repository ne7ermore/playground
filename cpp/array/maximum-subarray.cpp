/**
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
**/

#include <vector>
#include <algorithm>

class Solution
{
  public:
    int maxSubArray(std::vector<int> &nums)
    {
        int res = nums[0], pre = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            pre = std::max(pre, 0);
            res = std::max(pre + nums[i], res);
            pre = pre + nums[i];
        }
        return res;
    }
};