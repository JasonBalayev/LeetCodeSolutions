class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        long long count=0;
        int n=nums.size();
        for (int i=0; i<n-1; i++) {
            int l=upper_bound(nums.begin()+i+1, nums.end(), lower-nums[i]-1) -nums.begin();
            int r=upper_bound(nums.begin()+i+1, nums.end(), upper-nums[i]) - nums.begin();
            count+=(r-l);
        }
        return count;
    }
};

//QED
//Problem 2563 (Medium of Count The Number Of Fair Pairs) - Jason Balayev (cpp)