#include<vector>
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int m=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            int d=abs(nums[i]-nums[(i+1)%n]);
            if(d>m)m=d;
        }
        return m;
    }
};

//QED
//Problem 3423 (Easy of Maximum Difference Between Adjacent Elements In A Circular Array) - Jason Balayev (cpp)