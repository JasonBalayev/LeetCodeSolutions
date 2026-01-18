class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for k in range(min(m,n),0,-1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    s=sum(grid[i+r][j+r]for r in range(k))
                    if sum(grid[i+r][j+k-1-r]for r in range(k))!=s:
                        continue
                    valid=True
                    for r in range(k):
                        if sum(grid[i+r][j:j+k])!=s:
                            valid=False
                            break
                    if valid:
                        for c in range(k):
                            if sum(grid[i+r][j+c]for r in range(k))!=s:
                                valid=False
                                break
                    if valid:
                        return k
        return 1

#QED
#Problem 1895 (Medium of Largest Magic Square) - Jason Balayev (python)