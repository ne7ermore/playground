"""
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

 

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
"""


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        counter = collections.Counter(A)

        for a in A:
            if a == 0 or counter[a] == 0:
                continue

            if a > 0:
                target = a*2
            elif a < 0:
                if a % 2 != 0:
                    return False
                target = a // 2

            if counter[target] < counter[a]:
                return False

            counter[target] = counter[target]-counter[a]
            counter[a] = 0

        return True
