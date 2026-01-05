class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total=neg=0
        min_abs=float('inf')
        for r in matrix:
            for v in r:
                total+=abs(v)
                neg+=v<0
                if abs(v)<min_abs:
                    min_abs=abs(v)
        return total if neg%2==0 else total-2*min_abs

#QED
#Problem 1975 (Medium of Maximum Matrix Sum) - Jason Balayev (python)