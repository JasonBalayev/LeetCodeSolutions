class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int min = *min_element(nums.begin(), nums.end());
        int max = *max_element(nums.begin(), nums.end());
        return max - min <= 2 * k ? 0 : max - min - 2 * k;
    }
};

//QED
//Problem 908 (Easy Of Smallest Range I) - Jason Balayev (cpp)