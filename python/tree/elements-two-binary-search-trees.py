"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8] 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, res = [], [], []

        def dfs(node, stack):
            if node:
                dfs(node.right, stack)
                stack.append(node.val)
                dfs(node.left, stack)

        dfs(root1, stack1)
        dfs(root2, stack2)
        n1, n2 = stack1.pop() if len(stack1) else None, stack2.pop() if len(stack2) else None
        while n1 is not None or n2 is not None:
            if n1 is not None and n2 is not None:
                if n1 < n2:
                    res.append(n1)
                    n1 = stack1.pop() if len(stack1) else None
                else:
                    res.append(n2)
                    n2 = stack2.pop() if len(stack2) else None
            elif n1 is not None:
                res.append(n1)
                n1 = stack1.pop() if len(stack1) else None
            elif n2 is not None:
                res.append(n2)
                n2 = stack2.pop() if len(stack2) else None
        return res
