/**
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"2": ["a","b","c"],
"3": ["d","e","f"],
"4": ["g","h","i"],
"5": ["j","k","l"],
"6": ["m","n","o"],
"7": ["p","q","r","s"],
"8": ["t","u","v"],
"9": ["w","x","y","z"]

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * **/

#include <string>
#include <vector>

using namespace std;

class Solution
{
    vector<string> nC{" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

  public:
    vector<string> letterCombinations(string digits)
    {
        vector<string> res;
        if (digits.empty())
            return res;
        backtrack(res, "", digits);
        return res;
    }

    void backtrack(vector<string> &res, string letter, string d)
    {
        if (d.size() == 1)
            for (auto &c : nC[d[0] - '0'])
                res.push_back(letter + c);
        else
        {
            for (auto &c : nC[d[0] - '0'])
                backtrack(res, letter + c, d.substr(1));
        }
    }
};