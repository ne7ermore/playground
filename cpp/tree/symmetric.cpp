/**

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
 * **/

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(0), right(0) {}
};

class Solution
{
  public:
    bool isSymmetric(TreeNode *root)
    {
        return root == 0 || check(root->left, root->right);
    }

    bool check(TreeNode *left, TreeNode *right)
    {
        if (left == 0 && right == 0)
            return true;
        else if (left && right)
        {
            return left->val == right->val && check(left->right, right->left) && check(left->left, right->right);
        }
        else
            return false;
    }
};