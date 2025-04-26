class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res =0
        last_outof_bounds=-1
        last_min=-1
        last_max=-1
        for i, num in enumerate(nums):
            if num<minK or num >maxK:
                last_outof_bounds=i
            else:
                if num==minK:
                    last_min=i
                if num==maxK:
                    last_max=i
                if last_min>last_outof_bounds and last_max>last_outof_bounds:
                    leftmost=min(last_min,last_max)
                    res+=leftmost-last_outof_bounds
        return res

#QED
#Problem 2444 (Hard) - Count Subarrays With Fixed Bounds - Jason Balayev (python)