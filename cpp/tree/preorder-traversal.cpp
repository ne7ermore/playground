/**
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].
 * **/

#include <vector>

class Node
{
  public:
    int val;
    std::vector<Node *> children;

    Node() {}

    Node(int _val, std::vector<Node *> _children)
    {
        val = _val;
        children = _children;
    }
};

class Solution
{
  public:
    std::vector<int> preorder(Node *root)
    {
        std::vector<int> res;
        dfs(root, res);
        return res;
    }

    void dfs(Node *node, std::vector<int> &res)
    {
        if (node != 0)
        {
            res.push_back(node->val);
            for (auto &c : node->children)
                dfs(c, res);
        }
    }
};