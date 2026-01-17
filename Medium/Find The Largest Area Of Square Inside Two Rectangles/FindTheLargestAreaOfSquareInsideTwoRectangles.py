class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n=len(bottomLeft)
        mx=0
        for i in range(n):
            for j in range(i+1,n):
                a1,b1=bottomLeft[i]
                c1,d1=topRight[i]
                a2,b2=bottomLeft[j]
                c2,d2=topRight[j]
                x1=max(a1,a2)
                y1=max(b1,b2)
                x2=min(c1,c2)
                y2=min(d1,d2)
                if x1<x2 and y1<y2:
                    side=min(x2-x1,y2-y1)
                    mx=max(mx,side*side)
        return mx
 
 #QED
 #Problem 3047 (Medium of Find The Largest Area Of Square Inside Two Rectangles) - Jason Balayev (python)