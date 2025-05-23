class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_p = ''
        for char in p:
            if not new_p or char != '*' or new_p[-1] != '*':
                new_p += char
        p = new_p
        
        if p=='*':
            return True
        if not p:
            return not s
        if not s and p and p != '*':
            return False
        
        m,n = len(s), len(p)
        prev_row = [False] * (n+1)
        prev_row[0] = True

        for j in range(1, n+1):
            if p[j-1] == '*':
                prev_row[j] = prev_row[j-1]
            else:
                break
            
        for i in range(1, m+1):
            curr_row = [False] * (n+1)
            for j in range(1,n+1):
                if p[j-1] == '*':
                    curr_row[j] = curr_row[j-1] or prev_row[j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    curr_row[j] = prev_row[j-1]    
            prev_row = curr_row
        return prev_row[n]
        
        # m,n = len(s), len(p)
        # dp = [[False] * (n+1) for x in range(m+1)]
        # dp[0][0] = True

        # for j in range(1, n+1):
        #     if p[j-1] == '*':
        #         dp[0][j] = dp[0][j-1]
        
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if p[j-1] == '*':
        #             dp[i][j] = dp[i][j-1] or dp[i-1][j]
        #         elif p[j-1] == '?' or s[i-1] == p[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        
        # return dp[m][n]
        
#QED
#Problem 44 (Hard Of Wildcard Matching) - Jason Balayev (python)