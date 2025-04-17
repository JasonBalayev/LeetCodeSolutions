class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        remainder=total_sum % k
        
        if remainder==0:
            return 0
        return remainder
    
#QED
#Problem 3512 (Easy of Minimum Operations to Make Array Sum Divisible by K) - Jason Balayev (python)