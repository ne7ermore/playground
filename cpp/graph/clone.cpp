/**
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors. 

Example:

  1 ----------- 2
  |             |
  |             |
  |             |
  3 ----------- 4

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
 * **/

#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Node
{
  public:
    int val;
    vector<Node *> neighbors;

    Node() {}

    Node(int _val, vector<Node *> _neighbors)
    {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution
{
    unordered_map<Node *, Node *> mappings;

  public:
    Node *cloneGraph(Node *node)
    {
        Node *newNode = new Node(node->val, {});
        mappings[node] = newNode;
        queue<Node *> qee;
        qee.push(node);
        while (!qee.empty())
        {
            Node *cur = qee.front();
            qee.pop();
            for (auto &nxtNode : cur->neighbors)
            {
                Node *newNxtNode;
                if (!mappings.count(nxtNode))
                {
                    mappings[nxtNode] = new Node(nxtNode->val, {});
                    qee.push(nxtNode);
                }
                mappings[cur]->neighbors.push_back(mappings[nxtNode]);
            }
        }
        return newNode;
    }
};