from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_nums1 = m - 1  
        last_nums2 = n - 1 
        last_merged = m + n - 1 
        
        while last_nums2 >= 0 and last_nums1 >= 0:
            if nums1[last_nums1] > nums2[last_nums2]:
                nums1[last_merged] = nums1[last_nums1]
                last_nums1 -= 1
            else:
                nums1[last_merged] = nums2[last_nums2]
                last_nums2 -= 1
            last_merged -= 1
        
        while last_nums2 >= 0:
            nums1[last_merged] = nums2[last_nums2]
            last_nums2 -= 1
            last_merged -= 1

#QED
#Problem 88 (Merge Sorted Array) - Jason Balayev (python)   