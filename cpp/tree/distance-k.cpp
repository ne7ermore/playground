/**
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

        3
      /   \
     5      1
    / \    / \
   6   2  0   8
      / \
     7   4

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
 * **/

#include <map>
#include <vector>
#include <queue>
#include <set>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(0), right(0) {}
};

class Solution
{
    std::map<TreeNode *, TreeNode *> m;
    std::queue<TreeNode *> q;
    std::set<TreeNode *> seen;
    std::vector<int> res;

  public:
    std::vector<int> distanceK(TreeNode *root, TreeNode *target, int K)
    {
        dfs(root);
        seen.insert(target);
        bfs(target, K);
        return res;
    }

    void dfs(TreeNode *node)
    {
        if (node->left)
        {
            m[node->left] = node;
            dfs(node->left);
        }

        if (node->right)
        {
            m[node->right] = node;
            dfs(node->right);
        }
    }

    void bfs(TreeNode *node, int K)
    {
        if (K == 0)
        {
            res.push_back(node->val);
        }
        else
        {
            auto p = m.find(node);
            if (p != m.end() && !seen.count(m[node]))
            {
                seen.insert(m[node]);
                bfs(m[node], K - 1);
            }

            if (node->left != 0 && !seen.count(node->left))
            {
                seen.insert(node->left);
                bfs(node->left, K - 1);
            }
            if (node->right != 0 && !seen.count(node->right))
            {
                seen.insert(node->right);
                bfs(node->right, K - 1);
            }
        }
    }
};