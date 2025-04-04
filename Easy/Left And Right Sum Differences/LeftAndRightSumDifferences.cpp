class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> result(nums.size());
        int leftSum = 0;
        int rightSum = accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size(); i++) {
            rightSum -= nums[i];
            result[i] = abs(leftSum - rightSum);
            leftSum += nums[i];
        }
        return result;      
    }
};

//QED
//Problem 2574 (Easy Of Left And Right Sum Differences) - Jason Balayev (cpp)