/**
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
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
    int findSecondMinimumValue(TreeNode *root)
    {
        std::vector<int> res = {INT_MAX, INT_MAX};
        dfs(root, res);
        if (res[1] == res[0] || res[1] == INT_MAX)
            return -1;
        else
            return res[1];
    }

  private:
    void dfs(TreeNode *node, std::vector<int> &res)
    {
        if (node != 0)
        {
            if (node->val != res[0])
            {
                if (node->val < res[1])
                {
                    if (node->val < res[0])
                    {
                        res[1] = res[0];
                        res[0] = node->val;
                    }
                    else
                    {
                        res[1] = node->val;
                    }
                }
            }
            dfs(node->left, res);
            dfs(node->right, res);
        }
    }
};