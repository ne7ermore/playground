/**
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
**/

class Solution {
    
    vector<vector<int>> res;
    vector<int> c_nums;
    
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> nums;
        backtrack(nums, candidates, target, 0);
        return res;
    }
    
private:
    void backtrack(vector<int> nums, vector<int> candidates, int k, int sum_nums) {
        if (sum_nums == k) res.push_back(nums);
        else if (sum_nums < k) {
            for (int i = 0; i < candidates.size(); i++) {
                if (sum_nums + candidates[i] <= k) {
                    c_nums = nums;
                    c_nums.push_back(candidates[i]);
                    vector<int> c_candidates(candidates.cbegin()+i, candidates.cend());
                    backtrack(c_nums, c_candidates, k, sum_nums + candidates[i]);                    
                }
            }

        }
    }    
};