class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        infinity=10**18
        dist=[[infinity]*26 for _ in range(26)]
        for i in range(26):
            dist[i][i]=0
        for a,b,c in zip(original,changed,cost):
            u=ord(a)-97
            v=ord(b)-97
            if c<dist[u][v]:
                dist[u][v]=c
        for k in range(26):
            dk=dist[k]
            for i in range(26):
                dik=dist[i][k]
                if dik==infinity:
                    continue
                di=dist[i]
                for j in range(26):
                    nd=dik+dk[j]
                    if nd<di[j]:
                        di[j]=nd
        total=0
        for s,t in zip(source,target):
            if s==t:
                continue
            d=dist[ord(s)-97][ord(t)-97]
            if d==infinity:
                return -1
            total+=d
        return total

#QED
#Problem 2976 (Medium of Minimum Cost To Convert String I) - Jason Balayev (python)