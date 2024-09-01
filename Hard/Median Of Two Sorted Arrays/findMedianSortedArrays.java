class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        
        if (len1 > len2) {
            return findMedianSortedArrays(nums2,nums1);
        }
        
        int left = 0, right = len1, halfLength = (len1 + len2 +1) /2;
        while (left <= right) {
            int divide1 = (left + right) / 2;
            int divide2 = halfLength - divide1;
            int maxLeft1 = (divide1 == 0) ? Integer.MIN_VALUE : nums1[divide1 -1];
            int minRight1 = (divide1 == len1) ? Integer.MAX_VALUE : nums1[divide1];
            int maxLeft2 = (divide2 == 0) ? Integer.MIN_VALUE : nums2[divide2 -1];
            int minRight2 = (divide2 == len2) ? Integer.MAX_VALUE : nums2[divide2];
            
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((len1 + len2) % 2==1) {
                    return Math.max(maxLeft1, maxLeft2);
                }
                return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) /2.0;
            } else if (maxLeft1 > minRight2) {
                right = divide1 -1; 
            } else {
                left = divide1 +1; 
            }
        }
        return 0.0;
    }
}

//QED
//Problem 4 (Median Of Two Sorted Arrays) - Jason Balayev (java)   