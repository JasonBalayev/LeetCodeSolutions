class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        sentinel=10**9
        dp=[[[sentinel]*(k+1)for _ in range(n)]for _ in range(m)]
        dp[0][0][k]=0
        value_min={}
        value_map={}
        for i in range(m):
            for j in range(n):
                v=grid[i][j]
                if v not in value_map:
                    value_map[v]=[]
                value_map[v].append((i,j))
        sorted_values=sorted(value_map.keys())
        for _ in range(m*n):
            updated=False
            for i in range(m):
                for j in range(n):
                    for t in range(k+1):
                        old=dp[i][j][t]
                        if i>0 and dp[i-1][j][t]<sentinel:
                            dp[i][j][t]=min(dp[i][j][t],dp[i-1][j][t]+grid[i][j])
                        if j>0 and dp[i][j-1][t]<sentinel:
                            dp[i][j][t]=min(dp[i][j][t],dp[i][j-1][t]+grid[i][j])
                        if dp[i][j][t]<old:
                            updated=True
            for i in range(m):
                for j in range(n):
                    for t in range(k):
                        if dp[i][j][t+1]<sentinel:
                            idx=0
                            while idx<len(sorted_values)and sorted_values[idx]<=grid[i][j]:
                                v=sorted_values[idx]
                                for x,y in value_map[v]:
                                    if(x!=i or y!=j):
                                        old=dp[x][y][t]
                                        dp[x][y][t]=min(dp[x][y][t],dp[i][j][t+1])
                                        if dp[x][y][t]<old:
                                            updated=True
                                idx+=1
            if not updated:
                break
        return min(dp[m-1][n-1])
        return min(dp[m-1][n-1])

#QED
#Problem 3509 (Hard of Minimum Cost Path With Teleportations) - Jason Balayev (python)
