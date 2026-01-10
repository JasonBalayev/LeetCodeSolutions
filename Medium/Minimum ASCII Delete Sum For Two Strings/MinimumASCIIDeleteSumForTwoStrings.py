class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n=len(s1),len(s2)
        prev=[sum(ord(s2[j])for j in range(i))for i in range(n+1)]
        for i in range(m):
            curr=[prev[0]+ord(s1[i])]
            for j in range(n):
                if s1[i]==s2[j]:
                    curr.append(prev[j])
                else:
                    curr.append(min(prev[j+1]+ord(s1[i]),curr[j]+ord(s2[j])))
            prev=curr
        return prev[n]

#QED
#Problem 712 (Medium Of Minimum ASCII Delete Sum For Two Strings) - Jason Balayev (python)
