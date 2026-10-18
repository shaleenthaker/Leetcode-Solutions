"""You are given an m x n matrix board where each cell is part of a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. 
In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. 
At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships)."""

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        numBoats = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (
                    board[i][j] == 'X'
                    and (i == 0 or board[i - 1][j] != 'X')
                    and (j == 0 or board[i][j - 1] != 'X')
                ):
                    numBoats += 1
                    
        return numBoats