class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff=nums[k-1]-nums[0]
        for i in range(1,len(nums)-k+1):
            diff=nums[i+k-1]-nums[i]
            if diff<min_diff:
                min_diff=diff
        return min_diff

#QED
#Problem 1984 (Easy of Minimum Difference Between Highest And Lowest Of K Scores) - Jason Balayev (python)