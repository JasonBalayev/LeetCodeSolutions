import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> pairedIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (pairedIndex.containsKey(target - num)) {
                return new int[] {i, pairedIndex.get(target - num)};
            }
            pairedIndex.put(num, i);
        }
        return new int[] {};
    }
}

//QED
//Problem 1 (Two Sum) - Jason Balayev (java)