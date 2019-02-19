/**
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
**/

#include <vector>
#include <string>

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
    std::vector<std::string> binaryTreePaths(TreeNode *root)
    {
        std::vector<std::string> ss;
        if (root == NULL)
            return ss;
        dfs(root, ss, std::to_string(root->val) + "");
        return ss;
    }

  private:
    void dfs(TreeNode *node, std::vector<std::string> &ss, std::string s)
    {
        if (node->left == NULL && node->right == NULL)
            ss.push_back(s);
        else
        {
            if (node->left != NULL)
                dfs(node->left, ss, s + "->" + std::to_string(node->left->val));
            if (node->right != NULL)
                dfs(node->right, ss, s + "->" + std::to_string(node->right->val));
        }
    }
};