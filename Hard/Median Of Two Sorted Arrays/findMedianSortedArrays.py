class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        left, right = 0, len1
        half_len = (len1 + len2 + 1) //2
        
        while left <= right:
            divide1 = (left + right) //2
            divide2 = half_len - divide1
            max_left1 = float('-inf') if divide1 == 0 else nums1[divide1 -1]
            min_right1 = float('inf') if divide1 == len1 else nums1[divide1]
            max_left2 = float('-inf') if divide2 == 0 else nums2[divide2 -1]
            min_right2 = float('inf') if divide2 == len2 else nums2[divide2]
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (len1 + len2) % 2==1:
                    return max(max_left1, max_left2)
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) /2.0
            elif max_left1 > min_right2:
                right = divide1 -1
            else:
                left = divide1 +1

#QED
#Problem 4 (Median Of Two Sorted Arrays) - Jason Balayev (python)   