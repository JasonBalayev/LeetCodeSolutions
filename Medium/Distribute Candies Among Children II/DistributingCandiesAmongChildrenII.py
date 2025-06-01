class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=(n+2)*(n+1)//2
        for k in range(1,4):
            l=n-k*(limit+1)
            if l<0:
                break
            curr=(l+2)*(l+1)//2
            coeff=3 if k<3 else 1
            if k%2==1:
                ans-=coeff*curr
            else:
                ans+=coeff*curr
        return ans

#QED
#Problem 2929 (Medium of Distribute Candies Among Children II) - Jason Balayev (python)