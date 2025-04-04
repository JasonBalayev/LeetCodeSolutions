class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        left = 0
        count = 0
        for i in range(n-1):
            left+=nums[i]
            right = total - left

            if (left - right) % 2 ==0:
                count +=1
        return count 

#QED
#Problem 3423 (Easy Of Count Partitions With Even Sum Difference) - Jason Balayev (python)  