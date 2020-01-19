/**
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {        
        vector<vector<int>> res;
        vector<int> levels;
        
        if (!root) return res;        
        
        int dire = 1;
        
        queue<TreeNode*> tq;
        tq.push(root);
        
        int size = 1;
        
        while(tq.size()) {            
            auto node = tq.front();
            tq.pop();
            
            levels.push_back(node->val);
            
            if (node->left)
                tq.push(node->left);
            if (node->right)
                tq.push(node->right);
            size--;
            
            if (size == 0) {
                size = tq.size();
                if (dire == -1) {
                    dire = 1;
                    reverse(levels.begin(),levels.end());
                } else dire = -1;
                
                res.push_back(levels);
                levels.clear();
            }            
        }
        
        return res;
    }
};