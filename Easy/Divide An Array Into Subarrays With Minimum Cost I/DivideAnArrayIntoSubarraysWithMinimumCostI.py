class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        right_min=[nums[n-1]]*(n+1)
        for i in range(n-2,0,-1):
            right_min[i]=min(nums[i+1],right_min[i+1])
        min_cost=nums[0]+nums[1]+right_min[1]
        for i in range(1,n-1):
            min_cost=min(min_cost,nums[0]+nums[i]+right_min[i])
        return min_cost

#QED
#Problem 3010 (Easy of Divide An Array Into Subarrays With Minimum Cost I) - Jason Balayev (python)