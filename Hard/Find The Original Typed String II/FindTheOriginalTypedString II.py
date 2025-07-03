class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod=10**9+7
        n=len(word)
        runs=[]
        cnt=1
        for i in range(1,n):
            if word[i]==word[i-1]:
                cnt+=1
            else:
                runs.append(cnt)
                cnt=1
        runs.append(cnt)
        r=len(runs) 
        total=1
        for L in runs:
            total=(total*L)%mod
        if r>=k:
            return total
        m=k   
        dp=[0]*m
        dp[0]=1
        for L in runs:
            diff=[0]*(m+1)
            for s in range(m):
                if dp[s]==0:
                    continue
                add=dp[s]
                start=s+1
                end=min(m-1,s+L)
                diff[start]=(diff[start]+add)%mod
                if end+1<m+1:
                    diff[end+1]=(diff[end+1]-add)%mod
            cur=0
            for i in range(m):
                cur=(cur+diff[i])%mod
                dp[i]=cur
        small=sum(dp[r:k])%mod   
        ans=(total-small)%mod
        return ans

#QED
#Problem 3333 (Hard of Find The Original Typed String II) - Jason Balayev (python)