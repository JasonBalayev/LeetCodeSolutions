class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        h=v=1
        hc=vc=1
        for i in range(1,len(hBars)):
            hc=hc+1 if hBars[i]==hBars[i-1]+1 else 1
            h=max(h,hc)
        for i in range(1,len(vBars)):
            vc=vc+1 if vBars[i]==vBars[i-1]+1 else 1
            v=max(v,vc)
        return min(h+1 if hBars else 0,v+1 if vBars else 0)**2

#QED
#Problem 2943 (Medium of Maximize Area Of Square Hole In Grid) - Jason Balayev (python)