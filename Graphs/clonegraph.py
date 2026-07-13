"""Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors."""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}
        def copy(node: Optional['Node']):
            if node in visited:
                return visited[node]
            val = node.val
            clone = Node(val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(copy(neighbor))
            return clone
        return copy(node)