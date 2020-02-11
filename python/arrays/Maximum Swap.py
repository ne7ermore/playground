"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [i for i in str(num)]
        for idx in range(len(num)-1):
            if num[idx] < num[idx+1]:
                max_id = {num[i]: i for i in range(idx+1, len(num))}
                max_value, max_i = max(
                    max_id.keys()), max_id[max(max_id.keys())]
                for i in range(idx+1):
                    if num[i] < max_value:
                        num[i], num[max_i] = num[max_i], num[i]
                        return int("".join(num))

        return int("".join(num))
