class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start,target,path):
            if target==0:
                res.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                helper(i, target-candidates[i], path)
                path.pop()
                
        helper(0, target, [])
        return res
    
#QED
#Problem 39 (Medium Of Combination Sum) - Jason Balayev (python)