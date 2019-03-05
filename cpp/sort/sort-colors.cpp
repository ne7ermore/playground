/**
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
 * **/

#include <vector>

using namespace std;

void swap(vector<int> &nums, int i, int j)
{
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

class Solution
{
  public:
    void sortColors(vector<int> &nums)
    {
        int n = nums.size();
        int idx = -1, r = n - 1;
        for (int l = 0; l < n; l++)
        {
            if (nums[l] != 0)
            {
                for (int i = l + 1; i < n; i++)
                {
                    if (nums[i] == 0)
                    {
                        swap(nums, i, l);
                        idx = l;
                        break;
                    }
                }
            }
        }

        for (int l = n - 1; l > idx; l--)
        {
            if (nums[l] != 2)
            {
                for (int i = l - 1; i > idx; i--)
                {
                    if (nums[i] == 2)
                    {
                        swap(nums, i, l);
                        break;
                    }
                }
            }
        }
    }
};