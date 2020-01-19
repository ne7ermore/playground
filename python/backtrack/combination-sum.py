"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(vec, candidates):
            vec_sum = sum(vec)
            if vec_sum == target:
                res.append(vec)

            elif vec_sum < target:
                for index, candi in enumerate(candidates):
                    if vec_sum + candi <= target:
                        cvec = vec.copy()
                        cvec.append(candi)
                        backtrack(cvec, candidates[index:])

        res = []
        backtrack([], candidates)
        return res
