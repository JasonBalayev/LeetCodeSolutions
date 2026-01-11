class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        height=[0]*(n+1)
        max_area=0
        for i in range(m):
            for j in range(n):
                height[j]=height[j]+1 if matrix[i][j]=="1"else 0
            stack=[]
            for j in range(n+1):
                while stack and height[j]<height[stack[-1]]:
                    h=height[stack.pop()]
                    w=j-stack[-1]-1 if stack else j
                    max_area=max(max_area,h*w)
                stack.append(j)
        return max_area

#QED
#Problem 85 (Hard of Maximal Rectangle) - Jason Balayev (python)
