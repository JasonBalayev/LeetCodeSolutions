class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        if rows<3 or cols<3:
            return 0
        count=0
        for i in range(rows-2):
            for j in range(cols-2):
                alt_grid=[grid[i+row][j:j+3]for row in range(3)]
                diag1=alt_grid[0][0]+alt_grid[1][1]+alt_grid[2][2]
                diag2=alt_grid[0][2]+alt_grid[1][1]+alt_grid[2][0]
                if diag1!=diag2:
                    continue
                magic_sum=diag1
                valid=True
                for row in range(3):
                    if sum(alt_grid[row])!=magic_sum:
                        valid=False
                        break
                if valid:
                    for col in range(3):
                        if alt_grid[0][col]+alt_grid[1][col]+alt_grid[2][col]!=magic_sum:
                            valid=False
                            break
                if valid:
                    nums=[alt_grid[row][col]for row in range(3)for col in range(3)]
                    if sorted(nums)==list(range(1,10)):
                        count+=1
                        
        return count

#QED
#Problem 840 (Medium of Magic Squares In Grid) - Jason Balayev (python)