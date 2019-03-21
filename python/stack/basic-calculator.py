'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''


class Solution:
    def calculate(self, s: str) -> int:
        def func(res):
            ous = []
            while res:
                cur = res.pop()
                if cur == "(":
                    break
                ous.append(cur)
            prev, cul = 0, "+"
            while ous:
                cur = ous.pop()
                if cur == "+" or cur == "-":
                    cul = cur
                else:
                    if cul == "+":
                        prev += int(cur)
                    else:
                        prev -= int(cur)
            return prev

        ins, count = [], 0
        s = [c for c in s if c != " "]
        for idx, c in enumerate(s):
            if c == " ":
                continue
            if c.isdigit():
                count += 1
            else:
                if count != 0:
                    ins += ["".join(s[idx-count:idx])]
                    count = 0
                ins.append(c)
        if count != 0:
            ins += ["".join(s[-count:])]

        res = []
        for c in ins:
            if c == ")":
                res.append(func(res))
            else:
                res.append(c)

        return func(res)
