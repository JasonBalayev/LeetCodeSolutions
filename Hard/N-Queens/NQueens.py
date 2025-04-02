class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_safe(row,col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i,j = row - 1, col -1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i,j = row - 1, col +1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def solve(row):
                if row == n:
                    sltn = [''.join(row) for row in board]
                    solutions.append(sltn)
                    return
                
                for col in range(n):
                    if is_safe(row,col):
                        board[row][col] = 'Q'
                        solve(row +1)
                        board[row][col] = '.'
        solve(0)
        return solutions
        
#QED
#Problem 51 (Hard Of N-Queens) - Jason Balayev (python)   
