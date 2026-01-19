class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n=len(mat),len(mat[0])
        prefix=[[0]*(n+1)for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1]=mat[i][j]+prefix[i][j+1]+prefix[i+1][j]-prefix[i][j]
        l,r=0,min(m,n)
        while l<=r:
            mid=(l+r)//2
            found=False
            for i in range(mid,m+1):
                for j in range(mid,n+1):
                    if prefix[i][j]-prefix[i-mid][j]-prefix[i][j-mid]+prefix[i-mid][j-mid]<=threshold:
                        found=True
                        break
                if found:
                    break
            if found:
                l=mid+1
            else:
                r=mid-1
        return r
 
#QED
#Problem 1292 (Medium of Maximum Side Length Of A Square With Sum Less Than Or Equal To Threshold) - Jason Balayev (python)
