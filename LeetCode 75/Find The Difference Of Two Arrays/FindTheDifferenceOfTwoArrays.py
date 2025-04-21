class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        return [list(set1-set2),list(set2-set1)]
    
#QED
#Problem 2215 (Easy of Find The Difference Of Two Arrays) - Jason Balayev (python)