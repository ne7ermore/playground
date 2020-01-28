"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def subword(i):
            if i not in cut_word:
                cut_word[i] = [s[i:j] + (tail and " "+tail) for j in range(
                    i+1, len(s)+1) if s[i:j] in wordDict for tail in subword(j)]

            return cut_word[i]

        cut_word = {len(s): [""]}
        subword(0)
        return cut_word[0]
