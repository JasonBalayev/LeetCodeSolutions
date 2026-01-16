class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h=[1]+sorted(hFences)+[m]
        v=[1]+sorted(vFences)+[n]
        if len(h)<len(v):
            hg={h[j]-h[i]for i in range(len(h))for j in range(i+1,len(h))}
            vg={v[j]-v[i]for i in range(len(v))for j in range(i+1,len(v))}
            common=hg&vg
        else:
            vg={v[j]-v[i]for i in range(len(v))for j in range(i+1,len(v))}
            hg={h[j]-h[i]for i in range(len(h))for j in range(i+1,len(h))}
            common=vg&hg
        return max(common)**2%(10**9+7)if common else-1

#QED
#Problem 2975 (Medium of Maximum Square Area By Removing Fences From A Field) - Jason Balayev (python)
