from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val=max(nums)
        n=len(nums)
        
        def count_most_val(arr: List[int], val: int, m: int) -> int:
            left=0
            count_v=0
            total_subarrs=0
            for right in range(len(arr)):
                if arr[right]==val:
                    count_v+=1
                while count_v>m:
                    if arr[left]==val:
                        count_v-=1
                    left+=1
                total_subarrs+=(right-left+1)
            return total_subarrs

        count_less_than_k=count_most_val(nums,max_val,k-1)
        count_most_n=count_most_val(nums,max_val,n)
        return count_most_n-count_less_than_k

#QED
#Problem 2962 (Medium Of Count Subarrays Where Max Element Appears At Least K Times) - Jason Balayev (python)
