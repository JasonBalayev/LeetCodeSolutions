class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1

#QED
#Problem 26 (Easy Of Remove Duplicates From Sorted Array) - Jason Balayev (python)