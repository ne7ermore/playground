/**
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
 * **/

#include <vector>

using namespace std;

class Solution
{
  public:
    void nextPermutation(vector<int> &nums)
    {
        int n = nums.size();
        if (n < 2)
            return;
        int p = n - 2;
        int prev = nums[n - 1];
        while (p >= 0 && nums[p] >= prev)
        {
            prev = nums[p];
            p--;
        }

        if (p == -1)
        {
            reverse(nums.begin(), nums.end());
            return;
        }

        int cid = n - 1;
        while (nums[cid] <= nums[p])
            cid--;

        int tmp = nums[p];
        nums[p] = nums[cid];
        nums[cid] = tmp;

        reverse(nums.begin() + p + 1, nums.end());
    }
};