/**
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
 * **/

#include <string>

using namespace std;

class Solution
{
  public:
    bool validPalindrome(string s)
    {
        int l = 0, r = s.length() - 1;
        while (l < r)
        {
            if (s[l] == s[r])
            {
                l++;
                r--;
            }
            else
            {
                int i1 = l, j1 = r - 1, i2 = l + 1, j2 = r;
                while (i1 < j1 && s[i1] == s[j1])
                {
                    i1++;
                    j1--;
                }
                while (i2 < j2 && s[i2] == s[j2])
                {
                    i2++;
                    j2--;
                }
                return i1 >= j1 || i2 >= j2;
            }
        }
        return true;
    }
};