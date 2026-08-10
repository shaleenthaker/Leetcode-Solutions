"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once."""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        xLen = len(board)
        yLen = len(board[0])
        length = len(word)
        def backtracking(index, x, y):
            nonlocal length
            nonlocal xLen
            nonlocal yLen
            val = board[x][y]
            if word[index] == val and index == length - 1:
                return True
            elif word[index] != val:
                return False
            board[x][y] = '0'
            for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
                if x+dx >= 0 and x+dx < xLen and y+dy >= 0 and y+dy < yLen and board[x+dx][y+dy] != '0' and backtracking(index+1, x+dx, y+dy):
                    return True
            board[x][y] = val
            return False
        for i in range(xLen):
            for j in range(yLen):
                if board[i][j] == word[0] and backtracking(0, i, j):
                    return True
        return False