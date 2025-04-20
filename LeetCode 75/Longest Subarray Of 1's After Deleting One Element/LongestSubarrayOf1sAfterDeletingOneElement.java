class Solution {
    public int longestSubarray(int[] nums) {
        int last =0;
        int curr=0;
        int max=0;
        for (int num:nums) {
            if(num==1) {
                curr++;
            } else {
                max=Math.max(max,last+curr);
                last=curr;
                curr=0;
            }
        }
        max=Math.max(max,last+curr);
        return max==nums.length ? max-1:max;
    }
}

//Second Solution
// class Solution {
//     public int longestSubarray(int[] nums) {
//         int l=0;
//         int zeros=0;
//         int max=0;
//         for (int r=0; r<nums.length; r++){
//             if (nums[r]==0){
//                 zeros++;
//             }
//             while(zeros>1){
//                 if (nums[l]==0){
//                     zeros--;
//                 }
//                 l++;
//             } 
//             max = Math.max(max,r-l);
//         } 
//         return max;
//     }
// }

//QED
//Problem 1493 (Medium of Longest Subarray Of 1's After Deleting One Element) - Jason Balayev (java)