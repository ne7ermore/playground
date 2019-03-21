/**
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
 * **/

#include <vector>
#include <queue>

using namespace std;

class Node
{
  public:
    int val;
    vector<Node *> children;

    Node() {}

    Node(int _val, vector<Node *> _children)
    {
        val = _val;
        children = _children;
    }
};

class Solution
{
  public:
    int maxDepth(Node *root)
    {
        if (root == 0)
            return 0;
        queue<Node *> q;
        int depth = 0, size;
        q.push(root);
        while (!q.empty())
        {
            size = q.size();
            depth++;
            for (int i = 0; i < size; i++)
            {
                auto node = q.front();
                q.pop();
                for (auto &child : node->children)
                {
                    if (child != 0)
                        q.push(child);
                }
            }
        }
        return depth;
    }
};