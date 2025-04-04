## first solution

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        stack = [(1, [])]
        res = []

        while stack:
            start, curr = stack.pop()
            if len(curr) == k:
                res.append(curr)
                continue
            
            for i in range(n, start -1, -1):
                comb= curr + [i]
                stack.append((i+1, comb))
        return res
    
## second solution

class Solution(object):
    def secondSolution(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        combination = list(combinations(range(1,n+1),k)) 
        return combination
    
#QED
#Problem 77 (Medium Of Combinations) - Jason Balayev (python)        