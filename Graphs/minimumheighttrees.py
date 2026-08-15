from collections import deque

"""A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf."""

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [edges[0][0], edges[0][1]]
        remaining = n
        neighbors = {}
        for edge in edges:
            neighbors.setdefault(edge[0], set()).add(edge[1])
            neighbors.setdefault(edge[1], set()).add(edge[0])
        q = deque()
        for key, value in neighbors.items():
            if len(value) == 1:
                q.append(key)

        while remaining > 2:
            leaf_count = len(q)
            remaining -= leaf_count
            for i in range(leaf_count):
                node = q.popleft()
                for val in neighbors[node]:
                    neighbors[val].remove(node)
                    if len(neighbors[val]) == 1:
                        q.append(val)

        return list(q)