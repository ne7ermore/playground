"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        kits = collections.defaultdict(int)
        kits[0] = 1
        sums = res = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums-k in kits:
                res += kits[sums-k]
            kits[sums] += 1

        return res
