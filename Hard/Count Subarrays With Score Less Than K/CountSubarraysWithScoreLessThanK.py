class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        curr_sum=0
        i=0
        for j in range(n):
            curr_sum+=nums[j]
            while i<=j and curr_sum*(j-i+1)>=k:
                curr_sum-=nums[i]
                i+=1
            ans+=j-i+1
        return ans

#QED
#Problem 2302 (Hard of Count Subarrays With Score Less Than K) - Jason Balayev (python)