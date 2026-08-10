"""Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        vals = {}
        for i, val in enumerate(inorder):
            vals[val] = i
        preorderIndex = 0
        def recurse(left, right):
            if left > right:
                return None
            nonlocal preorderIndex
            root = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            index = vals[root.val]
            root.left = recurse(left, index-1)
            root.right = recurse(index+1, right)
            return root

        return recurse(0, len(preorder)-1)