/**
For an undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). 
Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. 
You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
 * **/

#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution
{
  public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>> &edges)
    {
        vector<unordered_set<int>> vs;
        vector<int> leaves;
        if (n == 1)
        {
            leaves.push_back(0);
            return leaves;
        }
        for (int i = 0; i < n; i++)
            vs.push_back(unordered_set<int>(0));
        for (auto &e : edges)
        {
            vs[e.first].insert(e.second);
            vs[e.second].insert(e.first);
        }

        for (int i = 0; i < n; i++)
        {
            if (vs[i].size() == 1)
                leaves.push_back(i);
        }

        while (true)
        {
            n -= leaves.size();
            vector<int> newLeaves;
            for (int node : leaves)
            {
                for (int n : vs[node])
                {
                    vs[n].erase(node);
                    if (vs[n].size() == 1)
                        newLeaves.push_back(n);
                }
            }
            if (newLeaves.empty())
                return leaves;
            leaves = newLeaves;
        }
    }
};