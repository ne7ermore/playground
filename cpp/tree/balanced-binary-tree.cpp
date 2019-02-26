/**
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
**/

#include <stddef.h>
#include <stdlib.h>
#include <algorithm>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
    bool bal = true;

  public:
    bool isBalanced(TreeNode *root)
    {
        if (root == NULL)
            return true;
        dfs(root);
        return bal;
    }

  private:
    int dfs(TreeNode *node)
    {
        if (node->left == NULL && node->right == NULL)
            return 0;
        else
        {
            int left = 0, right = 0;
            if (node->left != NULL)
                left = dfs(node->left) + 1;
            if (node->right != NULL)
                right = dfs(node->right) + 1;
            if (abs(left - right) > 1)
                bal = false;
            return std::max(right, left);
        }
    }
};
