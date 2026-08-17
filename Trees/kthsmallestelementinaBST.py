"""Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        visited = 0
        answer = None
        found = False
        def traverse(node):
            nonlocal found
            nonlocal visited
            nonlocal answer
            if not node or found:
                return
            traverse(node.left)
            visited += 1
            if visited == k:
                answer = node.val
                found = True
            traverse(node.right)
        traverse(root)
        return answer