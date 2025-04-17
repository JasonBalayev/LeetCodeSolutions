class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int count=0;
        int n=nums.size();
        for (int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                if (nums[i]==nums[j] && (i*j) % k==0) {
                    count++;
                }
            }
        }
        return count;
    }
};

//QED
//Problem 2176 (Easy of Count Equal and Divisible Pairs in an Array) - Jason Balayev (cpp)  