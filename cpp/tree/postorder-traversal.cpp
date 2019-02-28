/**
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].
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
    std::vector<int> postorder(Node *root)
    {
        std::vector<int> res;
        dfs(root, res);
        return res;
    }

    void dfs(Node *node, std::vector<int> &res)
    {
        if (node != 0)
        {
            for (auto &c : node->children)
                dfs(c, res);
            res.push_back(node->val);
        }
    }
};