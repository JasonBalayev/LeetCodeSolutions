class Solution {
    public int longestSubarray(int[] nums) {
        int l=0;
        int zeros=0;
        int max=0;
        for (int r=0; r<nums.length; r++){
            if (nums[r]==0){
                zeros++;
            }
            while(zeros>1){
                if (nums[l]==0){
                    zeros--;
                }
                l++;
            } 
            max = Math.max(max,r-l);
        } 
        return max;
    }
}

//QED
//Problem 1493 (Medium of Longest Subarray Of 1's After Deleting One Element) - Jason Balayev (java)