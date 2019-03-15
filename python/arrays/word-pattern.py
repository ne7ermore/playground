'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class Solution:
    def wordPattern(self, pattern, str):
        strs = str.split()
        ps = list(pattern)
        if len(strs) != len(ps):
            return False
        m = dict()
        bm = dict()
        for p, s in zip(strs, ps):
            if (p in m and m[p] != s) or (s in bm and bm[s] != p):
                return False
            m[p] = s
            bm[s] = p
        return True
