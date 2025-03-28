class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        can_match = [[False] * n for c in range(m)]
        can_match[0][0] = True

        for j in range(2, n):
            if p[j-1] == '*':
                can_match[0][j] = can_match[0][j-2]
            
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    can_match[i][j] = can_match[i-1][j-1]
                elif p[j-1] == '*':
                    can_match[i][j] = can_match[i][j-2]
                    prev_char = p[j-2]
                    if prev_char == '.' or prev_char == s[i-1]:
                        can_match[i][j] = can_match[i][j] or can_match[i-1][j]
        return can_match[m-1][n-1]
    
#QED
#Problem 10 (Hard Of Regular Expression Matching) - Jason Balayev (python)   