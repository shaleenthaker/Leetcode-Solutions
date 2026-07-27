from collections import deque

"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1."""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        xLen = len(grid)
        yLen = len(grid[0])
        freshCount = 0
        q = deque()

        for i in range(xLen):
            for j in range(yLen):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        minutes = 0

        while q:
            length = len(q)
            infected = False
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < xLen and 0 <= nc < yLen and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        infected = True
                        freshCount -= 1
            if infected:
                minutes += 1

        if freshCount != 0:
            return -1
        else:
            return minutes