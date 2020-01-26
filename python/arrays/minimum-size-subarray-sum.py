"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        len_n = len(nums)
        res = len_n+1
        left = right = 0
        while left < len_n:
            if sum(nums[left:right+1]) < s:
                if right < len_n:
                    right += 1
                else:
                    break

            else:
                res = min(res, right+1-left)
                left += 1
        return res if res != len_n+1 else 0
