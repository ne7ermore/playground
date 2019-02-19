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