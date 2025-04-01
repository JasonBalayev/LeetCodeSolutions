class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = [1]
            if i > 0:
                prev_row = res[i-1]
                for j in range(1,i):
                    row.append(prev_row[j-1] + prev_row[j])
                if i > 0:
                    row.append(1)
            res.append(row)
        return res
        
#QED
#Problem 118 (Easy Of Pascal's Triangle) - Jason Balayev (python)