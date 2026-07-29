"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        def recurse(root):
            if not root:
                return None
            right = recurse(root.right)
            left = recurse(root.left)
            nonlocal ancestor
            if root == p or root == q:
                if right is not None or left is not None:
                    ancestor = root 
                return root
            if right is not None and left is not None:
                ancestor = root
            elif right is not None:
                return right
            else:
                return left
        recurse(root)
        return ancestor
            