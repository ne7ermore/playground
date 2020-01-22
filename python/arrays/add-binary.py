"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ml = len(a) if len(a) > len(b) else len(b)
        c = ["0"] * (ml+1)

        a = (ml-len(a)+1)*"0" + a
        b = (ml-len(b)+1)*"0" + b

        tmp = 0
        for idx in range(ml, -1, -1):
            sub_a, sub_b = a[idx], b[idx]
            sub = int(sub_a) + int(sub_b) + tmp
            tmp = sub // 2

            c[idx] = str(sub % 2)

        if c[0] == "0":
            return "".join(c[1:])

        return "".join(c)
