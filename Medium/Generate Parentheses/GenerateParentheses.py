class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(s, left, right):
            if len(s) == 2 *n:
                res.append(''.join(s))
                return
            if left < n:
                s.append('(')
                helper(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                helper(s, left, right +1)
                s.pop()
        
        helper([],0,0)
        return res
    
#QED
#Problem 22 (Medium Of Generate Parentheses) - Jason Balayev (python)
