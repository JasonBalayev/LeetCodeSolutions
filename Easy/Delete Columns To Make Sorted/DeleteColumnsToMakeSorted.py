class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row,col=len(strs),len(strs[0])
        delete=0
        for c in range(col):
            for r in range(row-1):
                if strs[r][c]>strs[r+1][c]:
                    delete+=1
                    break
        return delete
#QED
#Problem 944 (Easy of Delete Columns To Make Sorted) - Jason Balayev (python)