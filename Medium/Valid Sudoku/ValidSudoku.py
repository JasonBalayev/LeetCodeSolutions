class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[set()for i in range(9)]
        c=[set()for i in range(9)]
        boxes=[set()for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                num=board[i][j]
                box_idx=(i//3)*3+(j//3)
                if num in r[i] or num in c[j] or num in boxes[box_idx]:
                    return False
                r[i].add(num)
                c[j].add(num)
                boxes[box_idx].add(num)
        return True

#QED
#Problem 36 (Medium of Valid Sudoku) - Jason Balayev (python)