"""Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        child_to_parent = {}
        seen = set()
        nodes = []
        def traverse(node):
            if not node:
                return
            if node.left:
                child_to_parent[node.left] = node
            if node.right:
                child_to_parent[node.right] = node
            traverse(node.left)
            traverse(node.right)
        def dfs(steps: int, node: TreeNode):
            if not node:
                return
            if node in seen:
                return
            elif steps == k:
                nodes.append(node.val)
                seen.add(node)
                return
            else:
                seen.add(node)
                dfs(steps+1, node.left)
                dfs(steps+1, node.right)
                if node in child_to_parent:
                    dfs(steps+1, child_to_parent[node])
        traverse(root)
        dfs(0, target)
        return nodes