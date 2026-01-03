class Solution:
    def numOfWays(self, n: int) -> int:
        mod=10**9+7
        abc,aba=6,6
        for i in range(n-1):
            abc,aba=(2*abc+2*aba)%mod,(2*abc+3*aba)%mod
        return (abc+aba)%mod

#QED
#Problem 1411 (Hard of Number Of Ways To Paint N x 3 Grid) - Jason Balayev (python)