class Solution {
    public int minOperations(int[] nums, int k) {
        for (int num: nums) {
            if (num<k) {
                return -1;
            }
        }
        Set<Integer> vals = new HashSet<>();
        for (int num: nums) {
            if (num>k) {
                vals.add(num);
            }
        }
        return vals.size();
    }
}

//QED
//Problem 3375 (Easy of Minimum Operations to Make Array Values Equal to K) - Jason Balayev (java)