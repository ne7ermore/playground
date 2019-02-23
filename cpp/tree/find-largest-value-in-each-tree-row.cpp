/**
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
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
    std::vector<int> largestValues(TreeNode *root)
    {
        std::vector<int> res;
        if (root == NULL)
            return res;

        dfs(res, 1, root);
        return res;
    }

  private:
    void dfs(std::vector<int> &res, int height, TreeNode *node)
    {
        if (node == NULL)
            return;

        if (res.size() < height)
            res.push_back(node->val);
        else
            res[height - 1] = std::max(res[height - 1], node->val);

        height++;
        dfs(res, height, node->left);
        dfs(res, height, node->right);
    }
};