"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        g = t = nums[0]
        while True:
            g = nums[g]
            t = nums[nums[t]]
            if g == t:
                break

        p1 = nums[0]
        p2 = g
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
