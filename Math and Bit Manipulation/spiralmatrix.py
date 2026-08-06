"""Given an m x n matrix, return all elements of the matrix in spiral order."""

# First attempt with recursion (not space optimal):
# class Solution:
#    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
#        output = []
#        xLen = len(matrix)
#        yLen = len(matrix[0])
#        def recurse(i, j, dir):
#            if i < 0 or j < 0 or i >= xLen or j >= yLen or matrix[i][j] == 'X':
#                return
#            output.append(matrix[i][j])
#            matrix[i][j] = 'X'
#            if dir == 'l':
#                if j-1 < 0 or matrix[i][j-1] == 'X':
#                    recurse(i-1, j, 'u')
#                else:
#                    recurse(i, j-1, 'l')
#            if dir == 'r':
#                if j+1 >= yLen or matrix[i][j+1] == 'X':
#                    recurse(i+1, j, 'd')
#                else:
#                    recurse(i, j+1, 'r')
#                
#            if dir == 'u':
#                if i-1 < 0 or matrix[i-1][j] == 'X':
#                    recurse(i, j+1, 'r')
#                else:
#                    recurse(i-1, j, 'u') 
#            if dir == 'd':
#                if i+1 >= xLen or matrix[i+1][j] == 'X':
#                    recurse(i, j-1, 'l')
#                else:
#                    recurse(i+1, j, 'd')         
#        recurse(0, 0, 'r')
#        return output

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        x = len(matrix)
        y = len(matrix[0])
        top, bottom = 0, x-1
        left, right = 0, y-1 
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                output.append(matrix[i][right])
            right -= 1

            if(top <= bottom):
                for i in range(right,left-1,-1):
                    output.append(matrix[bottom][i])
                bottom-=1

        
            if(left <= right):
                for i in range(bottom,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
        return output
