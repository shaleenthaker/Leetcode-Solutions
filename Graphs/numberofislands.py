"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water."""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        xLen = len(grid)
        yLen = len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= xLen or c >= yLen or grid[r][c] == 'X' or grid[r][c] == '0':
                return
            else:
                grid[r][c] = 'X'
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(r + dr, c + dc)
        count = 0
        for i in range(xLen):
            for j in range(yLen):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count