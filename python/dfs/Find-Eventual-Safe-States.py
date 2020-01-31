"""
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res, len_g = [], len(graph)
        if len_g == 0:
            return res
        status = [0]*len_g

        def dfs(start):
            if status[start] != 0:
                return status[start] == 1
            status[start] = 2
            for i in graph[start]:
                if not dfs(i):
                    return False

            status[start] = 1
            return True

        for i in range(len_g):
            if dfs(i):
                res.append(i)
        return res
