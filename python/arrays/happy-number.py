"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            count = 0
            while num:
                y = num % 10
                num = num//10
                count += y*y
            return count

        seen = set()

        while True:
            if n == 1:
                return True

            if n in seen:
                return False

            seen.add(n)
            n = square(n)
