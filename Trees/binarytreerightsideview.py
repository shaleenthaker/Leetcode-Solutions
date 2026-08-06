from collections import deque

"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        output = []
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == level_size-1:
                    output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return output