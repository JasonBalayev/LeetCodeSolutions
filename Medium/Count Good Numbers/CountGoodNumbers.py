class Solution:
    def countGoodNumbers(self, n: int) -> int:

        m = 10**9+7
        even = (n+1)//2
        odd = n//2

        def power(x,n,mod):
            if n==0:
                return 1
            half = power(x,n//2,mod)
            if n%2 ==0:
                return (half*half) % mod
            else:
                return (half*half*x) % mod
        return (pow(5,even,m) * pow(4, odd, m)) % m

#QED
#Problem 1922 (Medium Of Count Good Numbers) - Jason Balayev (python)