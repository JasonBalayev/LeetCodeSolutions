class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        for n in nums:
            s=c=0
            d=1
            while d*d<=n and c<5:
                if n%d==0:
                    s+=d
                    c+=1
                    if d!=n//d:
                        s+=n//d
                        c+=1
                d+=1
            if c==4:
                ans+=s
        return ans
    
#QED
#Problem 1390 (Medium of Four Divisors) - Jason Balayev (python)