class Solution(object):
    def twoSum(self, nums, target):
        paired_index= {}
        for i, num in enumerate(nums):
            if target - num in paired_index:
                return [i, paired_index[target-num]]
            paired_index[num] = i

#QED
#Problem 1 (Two Sum) - Jason Balayev (python)