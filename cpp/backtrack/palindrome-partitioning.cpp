/**
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
 * **/

#include <vector>
#include <string>

using namespace std;

class Solution
{
    vector<vector<string>> res;

  public:
    vector<vector<string>> partition(string s)
    {
        vector<string> progress;
        backtrack(s, 0, progress);
        return res;
    }

    bool ispalindrome(string s)
    {
        int l = 0;
        int r = s.size() - 1;
        while (l < r)
        {
            if (s[l] != s[r])
                return false;
            r--;
            l++;
        }
        return true;
    }

    void backtrack(string s, int idx, vector<string> progress)
    {
        if (idx == s.size())
            res.push_back(progress);
        else
        {
            for (int i = 1; i <= s.size() - idx; i++)
            {
                string sub = s.substr(idx, i);
                if (ispalindrome(sub))
                {
                    progress.push_back(sub);
                    backtrack(s, idx + i, progress);
                    progress.pop_back();
                }
            }
        }
    }
};