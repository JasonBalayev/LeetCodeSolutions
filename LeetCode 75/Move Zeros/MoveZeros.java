class Solution {
    public void moveZeroes(int[] nums) {
        int nonZerosIdx = 0;
        for (int i=0; i<nums.length; i++) {
            if (nums[i]!=0) {
                nums[nonZerosIdx] = nums[i];
                nonZerosIdx++;
            }
        }
        for (int i=nonZerosIdx; i <nums.length; i++) {
            nums[i]=0;
        }
    }
}

//QED
//Problem 283 (Easy of Move Zeros) - Jason Balayev (java)