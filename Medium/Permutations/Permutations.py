class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res= []

        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            curr = nums.pop(0)
            permutation = self.permute(nums)
            for perm in permutation:
                perm.append(curr)
            res.extend(permutation)
            nums.append(curr)
        return res

#QED
#Problem 46 (Medium Of Permutations) - Jason Balayev (python)
