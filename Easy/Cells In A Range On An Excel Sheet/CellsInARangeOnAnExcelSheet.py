class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        column1, row1 = s[0], s[1]
        column2, row2 = s[3], s[4]

        res=[]
        for col in range(ord(column1), ord(column2) + 1):
            for row in range(int(row1), int(row2) + 1):
                res.append(chr(col) + str(row))
        return res 
            
#QED
#Problem 2194 (Easy Of Cells In A Range On An Excel Sheet) - Jason Balayev (python)