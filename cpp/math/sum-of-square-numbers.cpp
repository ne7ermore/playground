/**
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
 * **/

#include <complex>

using namespace std;

class Solution
{
  public:
    bool judgeSquareSum(int c)
    {
        long int left = 0, right = (int)sqrt(c);
        while (left <= right)
        {
            long int cur = left * left + right * right;
            if (cur < c)
                left++;
            else if (cur > c)
                right--;
            else
                return true;
        }
        return false;
    }
};