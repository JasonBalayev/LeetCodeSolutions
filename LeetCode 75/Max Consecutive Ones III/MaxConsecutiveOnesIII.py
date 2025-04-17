class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        max_len=0
        zeros=0

        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
        
#QED
#Problem 1004 (Medium of Max Consecutive Ones III) - Jason Balayev (python)