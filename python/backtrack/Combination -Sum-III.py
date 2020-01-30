"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(candidates, nums):
            if sum(nums) > n or len(nums) > k:
                return

            if len(nums) == k and sum(nums) == n:
                res.append(nums)

            elif len(nums) < k:
                for idx in range(len(candidates)):
                    backtrack(candidates[idx+1:], [candidates[idx]]+nums)

        res = []
        candidates = [i for i in range(1, min(n+1, 10))]
        backtrack(candidates, [])
        return res
