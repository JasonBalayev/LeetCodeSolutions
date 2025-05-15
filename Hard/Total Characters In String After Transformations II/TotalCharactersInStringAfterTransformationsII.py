class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod=10**9 + 7
        size=26
        def mult(a,b):
            rows=len(a)
            cols1=len(a[0])
            cols2=len(b[0])
            res=[[0]*cols2 for i in range(rows)]
            for i in range(rows):
                for j in range(cols2):
                    sum=0
                    for k in range(cols1):
                        sum=(sum+a[i][k]*b[k][j])%mod
                    res[i][j]=sum
            return res
        def power(base,exp):
            res=[[0]*size for i in range(size)]
            for i in range(size):
                res[i][i]=1
            p=base
            e=exp
            while e>0:
                if e%2==1:
                    res=mult(res,p)
                p=mult(p,p)
                e//=2
            return res
        if t==0:
            return len(s)
        mat=[[0]*size for i in range(size)]
        for i in range(size):
            count=nums[i]
            for j in range(1,count+1):
                pos=(i+j)%size
                mat[i][pos]=1
        steps=power(mat,t)
        lens=[0]*size
        for i in range(size):
            sum=0
            for j in range(size):
                sum=(sum+steps[i][j])%mod
            lens[i]=sum
        counts=[0]*size
        for c in s:
            idx=ord(c)-ord('a')
            counts[idx]+=1
        ans=0
        for i in range(size):
            val=(counts[i]*lens[i])%mod
            ans=(ans+val)%mod
        return ans

#QED
#Problem 3337 (Hard Of Total Characters In String After Transformations II) - Jason Balayev (python)