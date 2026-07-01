"""Given the root of a binary tree, invert the tree, and return its root."""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None: # Bottom of the tree
            return
        root.left, root.right = root.right, root.left # Quick python syntax to swap two elements
        self.invertTree(root.right) # Recurse into right child
        self.invertTree(root.left) # Recurse into left child
        return root # This goes back up the tree, so our eventual return will be the root of the tree