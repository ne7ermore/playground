/**
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
**/

#include <vector>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
  public:
    std::vector<int> inorderTraversal(TreeNode *root)
    {
        std::vector<int> res;
        dfs(root, res);
        return res;
    }

    void dfs(TreeNode *node, std::vector<int> &res)
    {
        if (node != 0)
        {
            dfs(node->left, res);
            res.push_back(node->val);
            dfs(node->right, res);
        }
    }
};